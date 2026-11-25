def squirrel_play(temp, is_summer):
    if (is_summer and 60<=temp<=100) or 60<=temp<=90:
        return True
    else:
        return False

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
print(squirrel_play(90, False))
print(squirrel_play(50, True))
print(squirrel_play(50, False))