def cigar_party(cigars, is_weekend):
    if (40<=cigars<=60) or (is_weekend and cigars>=40):
        return True
    else:
        return False

print(cigar_party(39, True))
print(cigar_party(61, False))
print(cigar_party(70, True))
print(cigar_party(60, False))