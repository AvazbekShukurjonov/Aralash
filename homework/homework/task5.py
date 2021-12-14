def calculate(x, y):
    sum = 0
    for i in range(x, y+1):
        sum += i
    return sum

print(calculate(10,12))
