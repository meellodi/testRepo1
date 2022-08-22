import math


arr = [1, 3]


def solution(nums, target):
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
            if i1 >= i2:
                print("y")
                return i1
        else:
            i2 = p
            if i2 <= 0:
                print("y")
                return i2
        p = math.floor((i2-i1)/2)+i1
        print(i1, i2, p)
    if target > nums[i1]:
        return i2
    else:
        return i1


# print(solution(arr, 5))
print(solution(arr, 2))
# print(solution(arr, 4))
