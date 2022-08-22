from unicodedata import name


def removeElement(nums, val):
    n = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == val:
            n += 1
            for j in range(len(nums)-1, i, -1):
                if nums[j] != nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
    print(nums)
    return(len(nums)-n)


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(removeElement([4, 5], 4))
