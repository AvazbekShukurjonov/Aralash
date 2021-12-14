def convertTemp(temp, C_or_F, to_C_or_F):
    if C_or_F=='C' and C_or_F=='F':
        print(temp + 56)
    if to_C_or_F=='F' and to_C_or_F=='C':
        print(temp - 56)
    return temp

print(convertTemp(30, 'C', 'F')) 