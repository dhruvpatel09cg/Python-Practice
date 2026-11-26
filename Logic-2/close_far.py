# def close_far(a, b, c):
#     if (a-1==b or a+1==b) and (c==b-2 or c==b+2):
#         return True
#     elif (a-1==c or a+1==c) and (b==c-2 or b==c+2):
#         return True
#     else:
#         return False

def close_far(a, b, c):
    if abs(a-b) <= 1:
        if abs(a-c) >= 2 and abs(b-c) >= 2:
            return True
        else:
            return False

    elif abs(a-c) <= 1:
        if abs(a-b) >= 2 and abs(c-b) >= 2:
            return True
        else:
            return False

    else:
        return False

print(close_far(10, 10, 8))
print(close_far(4, 3, 5))
print(close_far(4, 5, 3))
print(close_far(-1, 10, 0))
print(close_far(1, 2, 3))
print(close_far(1, 2, 10))
print(close_far(8, 9, 10))