def dNcArraySum(arr):
    if (len(arr) == 1):
        return arr[0]
    else:
        return dNcArray1(arr[:len(arr)-1])+arr[-1]


def arrSum(arr):
    result = 0
    for i in arr:
        result += i
    return result


arr = [0, 1, 2, 3, 4, 5, 6, 7]
print(dNcArray1(arr))
print(arrSum(arr))
