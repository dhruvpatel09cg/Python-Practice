def make_tags(tag, word):
    return "<"+tag+">"+word+"<"+"/"+tag+">"

print(make_tags("h3","Welcome!"))