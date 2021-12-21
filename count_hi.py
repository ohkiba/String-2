def count_hi(str):
    x=0
    count=0
    while x<len(str)-1:
        if str[x]=="h" and str[x+1]=="i":
            count+=1
        x+=1
    return count
