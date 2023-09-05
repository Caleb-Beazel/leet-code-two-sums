def twoSum(nums, target):
    sum_to_target = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    if i not in sum_to_target:
                        sum_to_target.append(i)
                    if i not in sum_to_target:
                        sum_to_target.append(j)

    return sum_to_target


print(twoSum([3,7,5], 12))