def near_hundred(n):
    if n in range(90,111) or n in range(190,211):
        return True
    return False

print(near_hundred(290))
print(near_hundred(210))