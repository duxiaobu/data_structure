import redis
from datetime import date, timedelta
import calendar

# redis 连接
r = redis.Redis(
    host="192.168.0.200",
    port=6379,
    db=3
)


# 检查参数装饰器
def check_input(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[1], int):
            raise ValueError(f"User_id must be int, and your input is {type(args[1])}")
        return func(*args, **kwargs)

    return wrapper


class RedisCheckIn:
    _private_key = "_check_in_"

    def __init__(self):
        pass

    @check_input
    def sign(self, user_id: int) -> int:
        # 用户签到
        return r.setbit(self._get_key(date.today()), user_id, 1)

    @check_input
    def sign_status(self, user_id: int) -> int:
        # 用户今日签到状态
        return r.getbit(self._get_key(date.today()), user_id)

    @check_input
    def week_sign_status(self, user_id: int) -> list:
        # 求出这个周的签到状况
        now = date.today()  # 2020-06-05
        # 周一是1 周日是7
        weekday = now.isoweekday()  # 5
        # 使用管道批量化操作
        with r.pipeline(transaction=False) as p:
            for d in range(weekday):
                check_day = now - timedelta(days=d)
                p.getbit(self._get_key(check_day), user_id)
            # 倒叙
            data = p.execute()[::-1]
        # 比如周三的时候我们只查3次getbit，然后剩下补0
        data.extend([0] * (7 - len(data)))
        return data

    @check_input
    def month_sing_status(self, user_id: int) -> list:
        # 求出这个月的某个用户签到状况
        now = date.today()
        day = now.day
        with r.pipeline(transaction=False) as p:
            for d in range(day):
                check_day = now - timedelta(days=d)
                p.getbit(self._get_key(check_day), user_id)
            data = p.execute()[::-1]
        # 获取当月天数，还没到的天数补0
        month_range = calendar.monthrange(now.year, now.month)
        data.extend([0] * (month_range[1] - len(data)))
        return data

    @check_input
    def week_sign_num(self, user_id: int) -> int:
        # 求出这个周的签到次数
        return sum(self.week_sign_status(user_id))

    @check_input
    def month_sign_num(self, user_id: int) -> int:
        # 求出这个月的签到次数
        return sum(self.month_sing_status(user_id))

    @check_input
    def today_sign_all_num(self) -> int:
        # 求出当天有多少用户签到
        return r.bitcount(self._get_key(date.today()))

    @staticmethod
    def _get_key(check_date):
        return f"check_in_{check_date}"


if __name__ == '__main__':
    redis_sign_in = RedisCheckIn()
    redis_sign_in.sign(100)  # 签到
    print(redis_sign_in.sign_status(100))   # 1表示已签到
    print(redis_sign_in.sign_status(101))   # 0表示未签到
    print(redis_sign_in.week_sign_status(100))   # userId为100的用户这周签到情况：[0, 0, 0, 0, 1, 0, 0]
    print(redis_sign_in.week_sign_num(100))   # 这周总共签到1次
