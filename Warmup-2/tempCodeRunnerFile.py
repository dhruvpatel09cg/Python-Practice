def string_match(a, b):
    count = 0
    for i in range(len(a)-1):
        a2 = a[i:i+2]
        b2 = b[i:i+2]
        if a2 == b2:
            count = count + 1
    return count