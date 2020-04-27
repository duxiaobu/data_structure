def getRow(rowIndex):
    result = [1]
    for i in range(1, rowIndex + 1):
        tmp = [1]
        for j in range(1, i):
            tmp += [pre[j - 1] + pre[j]]
        # 加入末尾的[1]
        result = tmp + [1]
        pre = result
    return result


print(getRow(1))
