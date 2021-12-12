# # print(set([1,1,1,1,1,1,1,1,2,2,3,4,5,66,7,7]))
# print(set(['elbek','elbek','Elbek']))



# def toDrict(*strings):
#     dict = {}
#     for i, string in enumerate(strings):
#         dict[f'{i}'] = string
#     return dict
# print(toDrict('Hello', 'ABC', '123'))



# def convertTrmp(temp, from_t, to):
#     if from_t == 'C':
#         return(temp * 1.8) + 32
#     else: return (temp * 1.8) / 1.8

# print()


# print({11,2,3,4,5,6})

# print(set([11,2,3,3,3,3,3,3]))





# def nearest_value(set, num):
#     newNums = []
#     arr = list(set)
#     for elem in set:
#         newNums.append(abs(num - elem))
#     return arr[newNums.index(min(newNums))]
             
# print(nearest_value({4,7,10,11,12,17}, 9))
# print(nearest_value({4,7,10,11,12,17}, 8))
# print(nearest_value({4,9, 7,8, 11,12,17}, 8))