def missing_char(str, n):
    if n in range(0,len(str)):
        return str[:n]+str[n+1:]
    return "Invalid"

print(missing_char('code', 2))