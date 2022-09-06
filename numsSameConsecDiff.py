def numsSameConsecDiffRecursive(x, k):
    results = []
    for i in range(10):
        lastDigit = int(str(x)[-1])
        if i - lastDigit == k or lastDigit - i == k:
            results.append(x*10+i)
    return results


def numsSameConsecDiff(n, k):
    result = [i for i in range(1, 10)]
    print(result)
    temp = []
    for i in range(n-1):
        if len(temp) == 0:
            for x in result:
                temp += numsSameConsecDiffRecursive(x, k)
            result = temp
            temp = []
        else:
            for x in temp:
                result += numsSameConsecDiffRecursive(x, k)
            temp = result
            result = []

    return temp if len(temp) > 0 else result


# numsSameConsecDiffRecursive(25, 3)
numsSameConsecDiff(3, 2)
