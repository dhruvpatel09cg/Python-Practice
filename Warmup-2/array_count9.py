def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count = count + 1
    return count

print(array_count9([32,9,9,43,5,9,54,3]))
print(array_count9([]))
print(array_count9([4, 2, 4, 3, 1]))
print(array_count9([1, 2, 9]))