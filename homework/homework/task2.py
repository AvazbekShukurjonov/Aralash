def calculate(x, y, function):
    if function.lower() == 'add':
        return x + y
    elif function.lower() == 'subtract':
        return x - y
    elif function.lower() == 'multipi':
        return x * y
    elif function.lower() == 'divide':
        return x / y
    else:
        return 'Error'

print(calculate(2, 5, 'divide'))
print(calculate(2, 5, 'multipi'))
print(calculate(2, 5, 'subtract'))
print(calculate(2, 5, 'add'))