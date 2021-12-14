def convertTemp(temp, from_t_, to):
    if from_t_ == 'C':
        return(temp*1.8) + 32
    else:
        return(temp*1.8)/1.8


print(convertTemp(30,'C', 'F'))
