def count_code(str):
    count=0
    x=0
    while x<len(str)-3:
        if str[x:x+2]=="co" and str[x+3]=="e":
            count+=1
        x+=1
    return count