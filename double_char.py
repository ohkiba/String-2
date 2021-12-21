def double_char(str):
    newStr=""
    for x in range(len(str)):
        newStr=newStr+str[x]+str[x]
    return newStr