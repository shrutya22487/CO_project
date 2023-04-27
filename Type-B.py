def movImm(lst): #00010 mov
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print ("00010","0",r,val)

def rightShift(lst): #01000 rs
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print ("01000","0",r,val)

def leftShift(lst): #01001 ls
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print ("01001","0",r,val)
