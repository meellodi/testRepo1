def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i == 0 or n > nums[i-1]:
            nums[i] = n
            i += 1
    return i


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
