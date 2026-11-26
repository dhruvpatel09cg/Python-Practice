# def no_teen_sum(a, b, c):
#     sum = 0
#     if not (13<=a<=14 or 17<=a<=19):
#         sum+=a
#     if not (13<=b<=14 or 17<=b<=19):
#         sum+=b
#     if not (13<=c<=14 or 17<=c<=19):
#         sum+=c
#     return sum

def no_teen_sum(a, b, c):
    def fix_teen(n):
        if n >= 13 and n <= 19:
            if n == 15 or n == 16:
                return n
            else:
                return 0
        else:
            return n
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(17, 18, 19))
print(no_teen_sum(2, 1, 15))
print(no_teen_sum(17, 18, 16))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 15, 2))