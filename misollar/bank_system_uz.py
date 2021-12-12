def inputCredentials():
    login = input('Loginni kiriting: ').strip().lower()
    password = input('Parolni kiriting ').strip()
    return login, password


def chekCredentials(L, p):
    if L == '' or p == '':
        return False
        
    else: return True

def readData():
    with open('./bankdata.txt','r',encoding='utf-8') as data:
        StructuredData = []
        lines = data.readlines()
        for line in lines:
            userData = line.strip().split(';')
            if not userData[0][0].isdigit():
                user = {}
                user['fullname']=userData[0]
                user['username']=userData[1]
                user['pasword']=userData[2]
                user['numOfAccs']=userData[3]
                user['accounts']=[]
                for i, line in enumerate(lines, 1):
                    accData = line.strip().split(';')
                if userData[0][0].isdigit():
                    print(userData(1))


                    for j in range(i, int(user['numOfAccs'])+1):
                            print(j)
                            user['accounts'].append(accData)
                # StructuredData.append(user)
                    # print(j, userDatum)
            
        for dt in StructuredData:
            print(dt)
                

                

def auth():
    print('Salom! Bizning raqamli bankimizga xush kelibsiz!')
    while True:
        login,password =  inputCredentials()
        credentialsCorrect=chekCredentials(login, password)
        if credentialsCorrect: break
        else: print("Login yoki parol noto'g'ri.Iltimos qaytadan kiriting")
        readData()

# auth()

readData()
