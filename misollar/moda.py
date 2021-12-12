def readData():
    with open('./bankdata.txt','r', encoding = 'utf-8') as data:
        structuredData=[]
        lines = data.readlines()
        for i, line in enumerate(lines,1):
            userData = line.strip().split(';')
            if not userData[0].isdigit():
                # user ={}
                # user['fullName'] = userData[0]
                # user['userlName'] = userData[1]
                # user['password'] = userData[2]
                # user['numOfAccs'] = userData[3]  
                # structuredData.append(user)
                cods = line.strip().split(';')
            if cods[0].isdigit():
                code={}
                code['cardcode'] = cods[0]
                code['sum']=cods[1]
                structuredData.append(code)
        
        print(structuredData)
        # for i in range(userData[0].isdigit, userData.isdigit[4]):

        
# def readData():
#     with open('./bankdata.txt','r', encoding = 'utf-8') as data:
#         structuredData=[]
#         lines = data.readlines()
#         for i, line in enumerate(lines,1):
#             cods = line.strip().split(';')
#             if cods[0].isdigit():
#                 code={}
#                 code['cardcode'] = cods[0]
#                 code['sum']=cods[1]
#                 structuredData.append(code)

    

    # print(structuredData)
    print(code)
    readData()



# def add():
    
#     with open('./bankdata.txt','r', encoding = 'utf-8') as data: