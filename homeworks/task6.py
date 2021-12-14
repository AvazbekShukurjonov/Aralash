def y(x):
    if x>=0:
        y = x**2+2*x-3
    if x<0:
        y = -x**2-2*x-3
    return y
print(y(12))