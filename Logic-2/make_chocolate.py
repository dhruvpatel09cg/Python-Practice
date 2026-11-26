def make_chocolate(small, big, goal):
    need_big=goal//5
    need_small=goal%5
    if goal>small+big*5:
        return -1
    elif small<need_small:
        return -1
    elif big>need_big:
        return goal-need_big*5
    else:
        return goal-big*5

print(make_chocolate(4, 1, 5))
print(make_chocolate(6, 2, 11))
print(make_chocolate(6, 1, 11))
print(make_chocolate(1000, 1000000, 5000006))
print(make_chocolate(5, 4, 9))