def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    else:
        return False

print(has23([3, 3]))
print(has23([4, 5]))
print(has23([3, 9]))