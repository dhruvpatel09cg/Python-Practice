def combo_string(a, b):
    if len(a)<len(b):
        return a+b+a
    elif len(b)<len(a):
        return b+a+b

print(combo_string("Hey","Gang"))
print(combo_string("Hi","ok"))
print(combo_string("Namaste","India"))
print(combo_string("","kk"))