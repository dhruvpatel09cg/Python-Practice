def array_front9(nums):
    if len(nums) < 4:
        if 9 in nums[0:len(nums)]:
            return True
        return False
    if len(nums) > 4:
        if 9 in nums[0:4]:
            return True
        return False