def lucky_sum(a, b, c):
    sum = 0
    if a!=13:
        sum+=a
    else:
      return sum
    if b!=13:
        sum+=b
    else:
      return sum
    if c!=13:
        sum+=c
    else:
      return sum
    return sum

print(lucky_sum(13, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 2, 3))
print(lucky_sum(8, 13, 2))
print(lucky_sum(7, 2, 1))
print(lucky_sum(13, 2, 13))