def array_front9(nums):
    if len(nums) <= 4:
        if 9 in nums[0:len(nums)]:
            return True
        return False
    if len(nums) > 4:
        if 9 in nums[0:4]:
            return True
        return False

print(array_front9([3, 5, 64, 9]))
print(array_front9([2,5,4,6]))
print(array_front9([4,6,2,4,2,9]))
print(array_front9([3,9,5,4,3,2,4,2,3,]))