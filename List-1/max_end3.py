def max_end3(nums):
    if nums[0]>=nums[-1]:
        return [nums[0], nums[0], nums[0]]
    elif nums[-1]>=nums[0]:
        return [nums[-1], nums[-1], nums[-1]]

print(max_end3([11, 5, 9]))
print(max_end3([2, 2, 2]))