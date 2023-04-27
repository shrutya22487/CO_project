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
      ["rs", "R1", "$12"],
      ["ls", "R1", "$13"],
      ["hlt"]]
addr=len(code)-1

for instr in code:
    op=instr[0]
    if op=="mov" and ("$" in instr[2]):
        movImm(instr)
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
    elif op=="hlt":
        halt()
