def out_func():
    msg = 'hello'

    def inner_func():
        nonlocal msg
        msg = 'world'
        print(f'inner msg:{msg}')

    print(f'outer1 msg: {msg}')
    inner_func()
    print(f'outer2 msg: {msg}')


if __name__ == '__main__':
    out_func()
