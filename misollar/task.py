# print(""""Nexia","Tico",'Dmas',ko\'rganlar qilar xavas""" )

# print(5**4)

# print(22%4)

# kv_t=125
# Per=print(125*4)
# yuzi=print(125**4)

# print(3.14*(12/2)**2)

# katet1=6
# katet2=7
# sum=0
# sum=(katet1**2)+(katet2**2)
# print(sum)

# a='hello world'
# print(a)

# xabar='Avaz'
# print(xabar)
# xabar='Avazbek'
# print(xabar)


# radius=5
# pi=3,14
# yuza= pi * radius**2
# print("Radiusi",radius,"ga teng doira yuzi=",yuza)

# kocha="Bog'bon"
# mahalla="Sag'bon"
# tuman="Bodomzor"
# vilyat="Samarqand"
# print(kocha + ' ' + 'ko\'chasi',mahalla + ' ' + 'mahallasi',tuman + ' '+'tumani',vilyat+' ''viloyati')


# kocha=input('Ko\'changizni nomi\n')
# mahalla=input('mahallangizni nomi\n')
# tuman=input('tumaningizni nomi\n')
# viloyat=input('viloyatingiz nomi\n')
# print(kocha + ' ' + 'ko\'chasi',mahalla + ' ' + 'mahallasi',tuman + ' '+'tumani', viloyat +' ''viloyati')

# num=int(input('son kirt'))
# print(f'siz kiritgan sonning kvadrati {num**2} ga, kubi esa {num**3} ga teng')


# tugilgan_yil=int(input('nechanchi yilda tugilgansiz  '))
# a=0
# a=2021-tugilgan_yil
# print(f'Demak sizning yoshingiz {a} da')


# num1=int(input('Birinchi sonni kiriting faqat ikkinchisidan katta bolsin  '))
# num2=int(input('Ikkinchi sonni kiritt  '))
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)

# ismlar=['Jasmina','Rayxona','Sevinch']
# print(ismlar[0],'qalesan ishlaring yaxshmi')
# print(ismlar[1],'tugilgan kuning bilan')
# print(ismlar[2],'charchamadinmi')


# davlatlar=['Amerika','Xitoy','russiya','indoneziya','ozbekiston']
# print(len(davlatlar))
# print(davlatlar)


# davlatlar=['Amerika','Xitoy','russiya','indoneziya','ozbekiston']
# print(sorted(davlatlar))


# davlatlar=['Amerika','Xitoy','russiya','indoneziya','ozbekiston']
# print(sorted(davlatlar,reverse=True))

# davlatlar=['Amerika','Xitoy','russiya','indoneziya','ozbekiston']
# davlatlar.reverse()
# print(davlatlar)


# taomlar=[]
# taomlar.append('osh')
# taomlar.append('qovurdoq')
# taomlar.append('manti')
# taomlar.append('moshxo\'rdi')
# taomlar.insert(0, 'mastva')
# taomlar.remove('osh')
# del taomlar[0]
# print(taomlar)


# bozorlik=['yog\'','un','piyoz','banan','gosht']
# mahsulot=bozorlik.pop(3)
# print('men ''' + mahsulot  + '' 'sotib oldim')
# print('olinmagan mahsulatllar: ',bozorlik)


# davlatlar=['Amerika','Xitoy','russiya','indoneziya','ozbekiston']
# davlatlar.sort(reverse=True)
# print(davlatlar)


# sonlar=list(range(120,1201,2))
# max_qiymat=max(sonlar)
# min_qiymat=min(sonlar)
# print(max_qiymat)
# print(min_qiymat)
# sum=max_qiymat-min_qiymat
# print(sum)


# sonlar=list(range(120,1201,2))

# print(len(sonlar))


# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# sonlar=list(range(120,1201,2))
# print(sonlar[: 20])
# print(sonlar[260:281])
# print(sonlar[521:])


# taomlar=['osh','qozonkabob','dapanji','honim','shshli']
# print(taomlar)


# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f'{son} ning kvadrati {son**2} ga teng')

# dostlar=[]
# print('5 ta yaqin dostingiz kim?')
# for n in range(5):
#     dostlar.append(input(f'{n+1}-ismini kirit: '))
#     print(dostlar)


# ismlar=['Xusnora','Madina','Sevinch','Jasmina','Aziza']
# for ism in ismlar:
#     print('salom',ism)
# print('kod 5 marta takrorlanadi')


# sonlar=list(range(11,100,2))
# for son in sonlar:
#     print(son**3)

# kinolar=[]
# print('sevimli 5 ta kinoyingizni kiring')
# for i in range(5):
#    kinolar.append(input(f'{i+1}-kino nomini kirit: '))
#    print(kinolar)


# n_odam=int(input('bugun nechta odam bilan uchrashdingiz '))
# ismlar=[]
# for n in range(n_odam):
#     ismlar.append(input(f'{n+1} suhbatlashgan odamingiz  kim    '))
# print(ismlar)


# avtolar=['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#     if avto=='bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# cars=['tayota','mazda','hyundai','gm','kia']
# for car in cars:
#     if car!='gm':
#         print(car.upper())
#     else:
#         print(car.title())


# a=int(input('son kiriting '))
# b=int(input('son kiriting '))
# if a==b:
#     print('sonlar teng')
# else:
#     print('sonlar teng emas')

# ism=[]
# odam=int(input('bugun nechta odam bilan korishdingiz  '))
# for i in range(1,odam + 1):
#     kim = input('kim:')
#     ism.append(kim)
# print(ism)


# a=int(input('Yoshingiz netchida  '))
# if a<=4 or a>60:
#     print('Siga bepul')
# elif a<=18:
#     print('10 000')
# elif a>18:
#     print('20 000')


# a=int(input('son kiriting  '))
# b=int(input('son kiriting  '))
# if a==b:
#     print('bu sonlar teng')
# elif a<b:
#     print(f'{b} soni katta')
# elif a>b:
#     print(f'{a} sooni katta')


# def toliq_ism(ism,familiya):
#     """Foydalanuvchi ismi va familiyasini jamlab chiqaruvchi funksiya """
#     print(f'Foydalanuvchi ismi: {ism.title()}\n'
#           f'Foydalanuvchi familasi: {familiya.title()}')
# toliq_ism('olim','ikromov')


# mahsulotlar=['sabzi','Ketchup','garimdori','malako','kalbasa','rolton','bodring','Anjir','sut','gosht']
# savat=[]
# narsa=int(input('nechta nars kerek'))
# for i in narsa:
#     print('nima kerak')


# def salom_ber(ism):
#     """salom beruvchi funksiya"""
#     print(f'Assalpmu alaykum xurmatli {ism.title}')
# salom_ber('hasan')
# salom_ber('Ali')


# print(salom_ber.__doc__)


# def reverse(list):
#     return list[::-1]
# print(reverse([]))


# def sum(a,b): return a+b
# sum=lambda a,b : a+b

# def ism_yosh(ism,):
#     print(f'Ismingiz nima {ism.title()}')
#     # print(f'yoshiniz netchida')
#     print(ism)


# def reverse(list):
#     return list[::-1]
# print(reverse([1,3,4,8]))


# maxsulot=['ketchup','marojni','makaaaron']


# def toDric(*strings):
#     add={}
#     for i, string in enumerate(strings):
#         add[f'{i}']=string
#     return add

# print(toDric('hello','azim'))



def calcSumBetwen(x,y,):
    sum=0
    for i in range(x,y+1):
        sum += i
    return sum
print(calcSumBetwen(10,12))




for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for m in range(0, 10):
                print(i, j, k, m)