def caught_speeding(speed, is_birthday):
    if (is_birthday and 0<=speed<=65) or 0<=speed<=60:
        return 0
    elif (is_birthday and 66<=speed<=85) or 61<=speed<=80:
        return 1
    else:
        return 2

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
print(caught_speeding(80, False))
print(caught_speeding(85, False))
print(caught_speeding(85, True))
print(caught_speeding(40, True))
print(caught_speeding(90, False))