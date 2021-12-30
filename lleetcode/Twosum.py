def twoSum(nums, target):
    for i in range(0, len(nums)+1):
        for j in range(i+1, len(nums)):

            if nums[i] + nums[j] == target:
                r = [i, j]

                return r

    return []


a = twoSum([2, 5, 5, 11, 6, 10, 10], 20)
print(a)
