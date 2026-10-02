def string_splosion(str):
    c = ""
    for i in range(len(str)):
        c = c + str[:i+1]
    return c

print(string_splosion("Hello"))