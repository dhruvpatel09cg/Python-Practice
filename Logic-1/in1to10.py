def in1to10(n, outside_mode):
    if outside_mode and 1<n<10:
        return False
    elif 1<=n<=10:
        return True
    elif outside_mode and (n<1 or n>10):
        return True
    else:
        return False

print(in1to10(-1, True))
print(in1to10(11, False))
print(in1to10(10, True))
print(in1to10(1, False))
print(in1to10(-99, True))
print(in1to10(1, True))