def love6(a, b):
    if a==6 or b==6 or a+b==6 or a-b==6 or b-a==6:
        return True
    else:
        return False

print(love6(1, 7))
print(love6(-2, -4))
print(love6(4, 5))
print(love6(3, 3))
print(love6(-4, -10))
print(love6(6, 4))
print(love6(3, 4))
print(love6(7, 1))
print(love6(1, 8))
print(love6(0, 9))