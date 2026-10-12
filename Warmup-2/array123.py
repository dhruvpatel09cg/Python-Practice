def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

print(array123([1,2,3]))
print(array123([3,5]))
print(array123([4,6,37,1,2,3]))
print(array123([8,35,65,4,3,2,5,6,6,6,]))