def not_string(str):
    if str[:3] == "not" or str[:3] == "Not":
        return str
    return "not "+str

print(not_string("me"))
print(not_string("Not enough"))