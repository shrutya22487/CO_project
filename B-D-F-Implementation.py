def binary(x,n):
    lst=["0" for i in range (n)]
    for i in range (n-1, -1, -1):
        lst[i]=str(x%2)
        x=x//2
    return "".join(lst)


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

def movReg(lst): #00011 mov
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("00011", "00000", reg1, reg2)
def divide(lst): #00111 div
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("00111", "00000", reg1, reg2)
def invert(lst): #01101 not
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("01101", "00000", reg1, reg2)
def compare(lst): #01110 cmp
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print ("01110", "00000", reg1, reg2)

def load(lst, addr): #00100 ld
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr, 7)
    print ("00100", "0", r,addr)
def store(lst, addr): #00101 st
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr,7)
    print ("00101", "0", r, addr)

def halt(): #11010 hlt
    print ("11010", "00000000000")

code=[["mov", "R1", "$12"],
      ["ld", "R1", "var_name1"],
      ["st", "R2", "var_name2"],
      ["not", "R1", "R2"],
      ["mov", "R1", "R2"],
      ["cmp", "R1", "R2"],
      ["rs", "R1", "$12"],
      ["ls", "R1", "$13"],
      ["div", "R3", "R4"],
      ["hlt"]]

addr=len(code)-1
for instr in code:
    op=instr[0]
    if op=="mov":
        if ("$" in instr[2]):
            movImm(instr)
        else:
            movReg(instr)
    elif op=="rs":
        rightShift(instr)
    elif op=="ls":
        leftShift(instr)
    elif op=="ld":
        addr+=1
        load(instr,addr)
    elif op=="st":
        addr+=1
        store(instr, addr)
    elif op=="div":
        divide(instr)
    elif op=="not":
        invert(instr)
    elif op=="cmp":
        compare(instr)
    elif op=="hlt":
        halt()
