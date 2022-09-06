from random import randint


def dNcQuickSort(arr):
    if (len(arr) > 1):
        pivotIndex = randint(0, len(arr)-1)
        pivot = arr[pivotIndex]
        lessThan = []
        moreEqualThan = []
        for i in range(len(arr)):
            if (i != pivotIndex):
                if (arr[i] < pivot):
                    lessThan.append(arr[i])
                else:
                    moreEqualThan.append(arr[i])
        return dNcQuickSort(lessThan)+[pivot]+dNcQuickSort(moreEqualThan)
    else:
        return arr


x = [0, 10, 5, 3, 4, 6, 7, 1, 9, 2, 8]
print(dNcQuickSort(x))
