def movReg(lst): #00011 mov
    reg1=binary(int(lst[1]),3)
    reg2=binary(int(lst[2],3))
    print ("00011", "00000", reg1, reg2)

def divide(lst): #00111 div
    reg3=binary(int(lst[1]),3)
    reg4=binary(int(lst[2]),3)
    print ("00111", "00000", reg3, reg4)

def invert(lst): #01101 not
    reg1=binary(int(lst[1]),3)
    reg2=binary(int(lst[2],3))
    print ("01101", "00000", reg1, reg2)

def compare(lst): #01110 cmp
    reg1=binary(int(lst[1]),3)
    reg2=binary(int(lst[2],3))
    print ("01110", "00000", reg1, reg2)
