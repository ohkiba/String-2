def xyz_there(str):
    xyzCheck=0
    x=0
    while x<len(str)-1:
        if str[x:x+3]=="xyz" and str[x-1]!=".":
            return True
        x+=1
    return False