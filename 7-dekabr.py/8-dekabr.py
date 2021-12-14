# ages = [10,20,30,5,50,21,90]

# filteredAges = filter(lambda age: age <=30, ages)
# print(list(filteredAges))


# def filter_ages(func, ages, tgt):
#     filteredAges=[]
#     for age in ages:
#         result = func(age, tgt)
#         if result: filteredAges.append(age)
#         result



# def calculator(func, a,b):
#     return func(a,b)


# def add(a, b):
#     return a+b


# def subtract(a, b):
#     return a-b

# def multiplay(a, b):
#     return a*b

# def divide(a,b):
#     return a/b

# print(calculator(add,2,3))
# print(calculator(subtract,2,3))
# print(calculator(multiplay,2,3))
# print(calculator(divide,2,3))



# countries = [
#     ['China', 1394015977],
#     ['United States', 329877505],
#     ['India', 1326093247],
#     ['Indonesia', 267026366],
#     ['Bangladesh', 162650853],
#     ['Pakistan', 233500636],
#     ['Nigeria', 214028302],
#     ['Brazil', 21171597],
#     ['Russia', 141722205],
#     ['Mexico', 128649565],
# ]



def countryfilter(func, countries):
    filteredCountry=[]
    for count in countries:
        result = func(count)
        if result: filteredCountry.append(count)
    return filteredCountry

def lessThan(country):
    return country[1] >list(filter(func, ))

