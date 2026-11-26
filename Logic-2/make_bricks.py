def make_bricks(small, big, goal):
    need_small = goal%5
    if goal>big*5+small or small<need_small:
        return False
    else:
        return True

print(make_bricks(6, 1, 11))
print(make_bricks(3, 1, 9))
print(make_bricks(40, 2, 50))
print(make_bricks(1000000, 1000, 1000100))
print(make_bricks(40, 1, 46))
print(make_bricks(20, 4, 39))
print(make_bricks(1, 1, 7))