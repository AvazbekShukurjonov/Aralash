# def format_tel(tel):
#     if(len(tel)==13):
#         return '{}{}{}{}({}{}) {}{}{}-{}{}-{}{}'.format(*list(tel))

# print(format_tel('+998974773825'))

# name='elbek'
# surname='Khakimbekov'

# print('Salom, {} {}'.format(name,surname))


# for i in range(10):
#     print(i)
# else:
#     print(-1)



# for i in range(0,20,2):
#     print(i)

# list=[]
# for i in range(20):
#     if i% 2==0:
#         print(i)



# import datetime
# print(datetime.datetime.now())


from datetime import datetime,timedelta,timezone

print(datetime.now(timezone(timedelta(hours=3))))


print(datetime)