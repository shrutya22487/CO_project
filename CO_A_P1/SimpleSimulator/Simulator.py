import sys
i , R0 , R1 , R2 , R3 , R4 , R5 , R6 , FLAGS =0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0
reg = {
    "000": globals()["R0"],
    "001": globals()["R1"],
    "010": globals()["R2"],
    "011": globals()["R3"],
    "100": globals()["R4"],
    "101": globals()["R5"],
    "110": globals()["R6"],
    "111": globals()["FLAGS"]
} 
command_list = sys.stdin.readlines()   # comment this out
#l = [ 'D:\\test2.txt' ] # remove this
#for file in l:   # remove for loop
#f = open( 'D:\\test2.txt' )
#command_list = f.readlines()
l = len(command_list)
for i in range(l):
    command_list[i] = command_list[i].strip()  # Remove trailing newline character


variables = []
def set_flags(FLAGS, index):
    FLAGS=list(binary(FLAGS, 16))
    FLAGS[index]=1
    FLAGS=list(map(str, FLAGS))
    FLAGS=decimal("".join(FLAGS))
    return FLAGS

def registers():
    s=''
    for j in reg:
        s+=binary(reg[j],16) + ' ' #gives the output of the registers as binary 16 bits
    return s
def binary(x,n): #x->Decimal number, n->No of bits
    lst=["0" for i in range (n)]
    for i in range (n-1, -1, -1):
        lst[i]=str(x%2)
        x=x//2
    y = "".join(lst)
    return y
def decimal(n): # converts from binary to decimal
    num, value , base = int( n ) , 0 , 1 
    tmp = num
    while( tmp != 0 ):
        l = tmp % 10
        tmp = tmp // 10
        value = value + l * base
        base *= 2
    return value
def add(instr):
    #print( instr[10:13] )
    reg2= reg[instr[10:13] ]
    reg3= reg[instr[13:16] ]
    reg1=instr[7:10]
    reg[reg1]= reg2 + reg3
    if reg[reg1] > (2**16 -1) or reg[reg1] < -(2**16):
        reg["111"]=set_flags(reg["111"], 12)
        reg[reg1] = binary(0,16)
    else:
        reg["111"]=0
    
    return i+1

def sub(instr):
    reg2 = reg[instr[10:13]]
    reg3 = reg[instr[13:]]
    reg1 = instr[7:10]
    reg[reg1] = reg2 - reg3
    if reg2 < reg3:
        reg["111"]=set_flags(reg["111"], 12)
        reg[reg1] = binary(0, 16)
    else:
        reg["111"]=0

    return i + 1

def mul(instr):
    reg2= reg[instr[10:13]]
    reg3= reg[instr[13:]]
    reg1=instr[7:10]
    reg[reg1]= reg2 * reg3
    if reg[reg1] > (2**16 -1) or reg[reg1] < -(2**16):
        reg["111"]=set_flags(reg["111"], 12)
        reg[reg1] = binary(0,16)
    else:
        reg["111"]=0
    
    return i+1

def bit_xor(instr):
    reg2=reg[instr[10:13]]
    reg3=reg[instr[13:]]
    reg1=instr[7:10]
    reg[reg1] = reg2 ^ reg3
    reg["111"]=0
    return i+1

def bit_or(instr):
    reg2=reg[instr[10:13]]
    reg3=reg[instr[13:]]
    reg1=instr[7:10]
    reg[reg1] = reg2 | reg3
    reg["111"]=0
    return i+1

def bit_and(instr):
    reg2=reg[instr[10:13]]
    reg3=reg[instr[13:]]
    reg1=instr[7:10]
    reg[reg1] = reg2 & reg3
    reg["111"]=0
    return i+1

def movImm(instr):
    reg1=instr[6:9]
    val=decimal(instr[9:])
    reg[reg1]=val
    reg["111"]=0
    return i+1

def mov_reg(instr):
    reg1=instr[10:13]
    reg2=reg[instr[13:]]
    reg[reg1]=reg2
    reg["111"]=0
    return i+1

def div(instr):
    reg3=reg[instr[10:13]]
    reg4=reg[instr[13:]]
    if reg4==0:
        reg["111"]=set_flags(reg["111"], 12)
        reg["000"]=0
        reg["001"]=0
        return i+1
    reg["000"]=reg3//reg4
    reg["001"]=reg3%reg4
    reg["111"]=0
    return i+1

def rs(instr):
    reg1=instr[6:9]
    val=decimal(instr[9:])
    reg[reg1]=reg[reg1]>>val
    reg["111"]=0
    return i+1

def ls(instr):
    reg1=instr[6:9]
    val=decimal(instr[9:])
    reg[reg1]=reg[reg1]<<val
    reg["111"]=0
    return i+1

def n_ot(instr):
    reg1=instr[10:13]
    reg2=reg[instr[13:]]
    temp=''
    reg2=binary(reg2,16)
    for bit in reg2:
        if bit=="0":
            temp+="1"
        else:
            temp+="0"
    reg[reg1]=decimal(temp)
    reg["111"]=0
    return i+1

def c_mp(instr):
    reg1=reg[instr[10:13]]
    reg2=reg[instr[13:]]
    if reg1<reg2:
        reg["111"]=set_flags(reg["111"], 13)
    elif reg1>reg2:
        reg["111"]=set_flags(reg["111"], 14)
    else:
        reg["111"]=set_flags(reg["111"], 15)
    return i+1
def ld(instr):
    reg1=instr[6:9]
    mem = int( instr[9:] )
    loc = decimal( mem ) - l 
    leng = len( variables )
    for j in range( leng , loc + 1 ):
        variables.append( 0 )
    reg[reg1]=variables[loc] #Review
    reg["111"]=0
    return i+1

def st(instr):
    mem = int( instr[9:] )
    reg1 = reg[ instr[6:9] ]
    loc = decimal( mem ) - l 
    leng = len( variables )
    for j in range( leng , loc + 1 ):
        variables.append( 0 )
    variables[ loc ] = reg1
    reg["111"]=0
    return i+1

def jmp(instr):   # "01111"
    mem_addr = instr[10:]
    reg["111"]=0
    return decimal(mem_addr)

def jlt(instr):  # "11100"
    if binary(reg["111"],16)[13] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
    reg["111"]=0
    return i+1
    
def jgt(instr):  # "11101"
    if binary(reg["111"],16)[14] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
    reg["111"]=0
    return i+1

def je(instr):  # "11111"
    if binary(reg["111"],16)[15] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
    reg["111"]=0
    return i+1

def hlt():
    reg["111"]=0
    return 0
def memory_dump():
    for i, cmd in enumerate(command_list):
        print( cmd.strip())
    length_of_variable = len( variables )
    for i in range( 0 , length_of_variable ):
        print( binary( variables[ i ]  , 16  ) )
    #print("CHeCK")
    for i in range(l , 128 - length_of_variable ):
        print('0000000000000000')

#------------------main-------------------#
instructions = {
    "00000": add,
    "00001": sub,
    "00010": movImm,
    "00011": mov_reg,
    "00100": ld,
    "00101": st,
    "00110": mul,
    "00111": div,
    "01000": rs,
    "01001": ls,
    "01010": bit_xor,
    "01011": bit_or,
    "01100": bit_and,
    "01101": n_ot,
    "01110": c_mp,
    "01111": jmp,
    "11100": jlt,
    "11101": jgt,
    "11111": je,
    "11010": hlt
}
i = 0
while ( command_list[i][:5]!='11010'):   #termination step is when we reach opcode of halt
    i = instructions[command_list[i][:5]](command_list[i])
    s=registers()
    print(binary(i-1,7)+"        "+s)       
#print( "check")
reg["111"] = 0
s = registers()
print(binary(i,7)+"        "+s)
memory_dump()
#print( variables )
#print("\n")
#f.close()
