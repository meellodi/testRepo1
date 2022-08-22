import math


def searchInsert(nums, target):
    arr = nums
    i1 = 0
    i2 = len(nums)
    p = math.floor((i2-i1)/2)
    print(i1, i2, p, nums[p])
    while (i2-i1) > 1:
        if nums[p] == target:
            return p
        elif nums[p] < target:
            i1 = p+1
        else:
            i2 = p
        p = math.floor((i2-i1)/2)+i1
    if i2 > i1 and target > nums[i1]:
        return i2
    else:
        return i1
