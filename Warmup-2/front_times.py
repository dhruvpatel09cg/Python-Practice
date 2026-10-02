def front_times(str, n):
    result = ""
    for i in range(n):
        result = result + str[0:3]
    return result

print(front_times("Jatin",5))