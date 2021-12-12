

def inputCredentials():     #inputCredentials - shaxsiy malumot
    login = input('Loginni kiriting: ').strip().lower()
    password = input('Parolni kiriting ').strip()
    return login, password


def checkCredentials(L,p):
    if L =='' or p =='': return False
    else: return True


def readData():
    with open('./bankdata.txt','r', encoding = 'utf-8') as data:
        structuredData=[]
        lines = data.readlines()
        for i, line in enumerate(lines,1):
            userData = line.strip().split(';')
            if not userData[0].isdigit():
                user ={}
                user['fullName'] = userData[0]
                user['userlName'] = userData[1]
                user['password'] = userData[2]
                user['numOfAccs'] = userData[3]  
                structuredData.append(user)
                # print(j, userDatum)
        print(structuredData)
    

def auth():
    print("Salom! Bizniing raqamli bankimizga xush kelibsiz!")
    while True:
        login, password = inputCredentials()
        credentialsCorrect = checkCredentials(login, password)
        if credentialsCorrect: break
        else: print("Login yoki parol bo'sh qoldirilgan.Iltimos qaytadan kiriting")
        readData()


# auth()
readData()