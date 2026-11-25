def near_ten(num):
    remainder = num%10
    if remainder<=2 or remainder>=8:
        return True
    else:
        return False

print(near_ten(11))
print(near_ten(158))
print(near_ten(17))
print(near_ten(155))
print(near_ten(22))
print(near_ten(19))