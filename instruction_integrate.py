def binary(x,n):
    lst=["0" for i in range (n)]
    for i in range (n-1, -1, -1):
        lst[i]=str(x%2)
        x=x//2
    return "".join(lst)


def movImm(lst): #00010 mov
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print ("00010"+"0"+r+val)
def rightShift(lst): #01000 rs
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print ("01000"+"0"+r+val)
def leftShift(lst): #01001 ls
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print ("01001"+"0"+r+val)

def movReg(lst): #00011 mov
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("00011"+"00000"+reg1+reg2)
def divide(lst): #00111 div
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("00111"+"00000"+reg1+reg2)
def invert(lst): #01101 not
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("01101"+"00000"+reg1+reg2)
def compare(lst): #01110 cmp
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("01110"+"00000"+reg1+reg2)

def load(lst, addr): #00100 ld
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr, 7)
    print ("00100"+"0"+r+addr)
def store(lst, addr): #00101 st
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr,7)
    print ("00101"+"0"+r+addr)
    

def jmp(lst,code):   # "01111"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            print("01111","0000",binary(i,7))
            break

def jlt(lst,code,flag):  # "11100"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag < 1:
                print("11100","0000",binary(i,7))
                break
            break

def jgt(lst,code,flag):  # "11101"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag > 1:
                print("11101","0000",binary(i,7))
                break
            break

def je(lst,code,flag):  # "11111"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag == 1:
                print("11111","0000",binary(i,7))
                break
            break

def halt(): #11010 hlt
    print ("11010"+"00000000000")
    
    
if (flag):
  
    
 
