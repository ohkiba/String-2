def cat_dog(str):
    catCheck=0
    dogCheck=0
    x=0
    while x<len(str)-1:
        if str[x:x+3]=="cat":
            catCheck+=1
        if str[x:x+3]=="dog":
            dogCheck+=1
        x+=1
    return (catCheck==dogCheck)