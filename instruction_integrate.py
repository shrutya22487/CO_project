def binary(x,n):
    lst=["0" for i in range (n)]
    for i in range (n-1, -1, -1):
        lst[i]=str(x%2)
        x=x//2
    return "".join(lst)

def movImm(lst): #00010 mov
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    f.write("00010"+"0"+r+val+"\n")
def rightShift(lst): #01000 rs
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    f.write("01000"+"0"+r+val+"\n")
def leftShift(lst): #01001 ls
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    f.write("01001"+"0"+r+val+"\n")

def movReg(lst): #00011 mov
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    f.write("00011"+"00000"+reg1+reg2+"\n")
def divide(lst): #00111 div
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    f.write("00111"+"00000"+reg1+reg2+"\n")
def invert(lst): #01101 not
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    f.write("01101"+"00000"+reg1+reg2+"\n")
def compare(lst): #01110 cmp
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    f.write("01110"+"00000"+reg1+reg2+"\n")

def load(lst, addr): #00100 ld
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr, 7)
    f.write("00100"+"0"+r+addr+"\n")
def store(lst, addr): #00101 st
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr,7)
    f.write("00101"+"0"+r+addr+"\n")

def jmp(lst,code):   # "01111"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            val = binary(i,7)
            f.write("01111"+"0000"+val+"\n")
            break

def jlt(lst,code,flag):  # "11100"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag < 1:
                val = binary(i,7)
                f.write("11100"+"0000"+val+"\n")
                break
            break

def jgt(lst,code,flag):  # "11101"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag > 1:
                val = binary(i,7)
                f.write("11101"+"0000"+val+"\n")
                break
            break

def je(lst,code,flag):  # "11111"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag == 1:
                val = binary(i,7)
                f.write("11111"+"0000"+val+"\n")
                break
            break

def halt(): #11010 hlt
    f.write("11010"+"00000000000"+"\n")

f=open("output.txt", "w")
f.close()
f=open("output.txt", "a")

'''
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
'''

addr=len(code)-1
if (flag_check):
    for instr in command_list:
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
        elif op == "jmp":
            jmp(instr,command_list)
        elif op == "jlt":
            jmp(instr,command_list,flag)
        elif op == "jgp":
            jmp(instr,command_list,flag)
        elif op == "je":
            jmp(instr,command_list,flag)
        elif op=="hlt":
            halt()

f.close()
    
 
