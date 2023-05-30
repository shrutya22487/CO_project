i , R0 , R1 , R2 , R3 , R4 , R5 , R6 , FLAGS =0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , '0000000000000000'
reg = { "000" : R0 , "001" : R1 , "010" : R2 , "011" : R3 , "100" : R4 , "101" : R5 , "110" : R6 , "111" : FLAGS }  
command_list=["0001000100000100", "0011100000001110", "1101000000000000"]
l = len ( command_list )
variables = [] 
def registers():
    s=''
    for j in reg:
        if j!="111":
            s+=binary(reg[j],16) + '\n' #gives the output of the registers as binary 16 bits
    s+=FLAGS
    return s
def binary(x,n): #x->Decimal number, n->No of bits
    lst=["0" for i in range (n)]
    for i in range (n-1, -1, -1):
        lst[i]=str(x%2)
        x=x//2
    return "".join(lst)
def decimal(n): # converts from binary to decimal
    num, value , base = int( n ) , 0 , 1 
    tmp = num
    while( tmp != 0 ):
        l = tmp % 10
        tmp = tmp // 10
        value = value + l * base
        base *= 2
    return value

def movImm(instr):
    reg1=instr[6:9]
    val=decimal(instr[9:])
    reg[reg1]=val
    global FLAGS
    FLAGS="0000000000000000"
    return i+1

def mov_reg(instr):
    reg1=instr[10:13]
    reg2=reg[instr[13:]]
    reg[reg1]=reg2
    global FLAGS
    FLAGS="0000000000000000"
    return i+1

def div(instr):
    global FLAGS
    reg3=reg[instr[10:13]]
    reg4=reg[instr[13:]]
    if reg4==0:
        FLAGS="0000000000001000"
        reg["000"]=0
        reg["001"]=0
        return i+1
    reg["000"]=reg3//reg4
    reg["001"]=reg3%reg4
    FLAGS="0000000000000000"
    return i+1

def rs(instr):
    reg1=instr[6:9]
    val=decimal(instr[9:])
    reg[reg1]=reg[reg1]>>val
    global FLAGS
    FLAGS="0000000000000000"
    return i+1

def ls(instr):
    reg1=instr[6:9]
    val=decimal(instr[9:])
    reg[reg1]=reg[reg1]<<val
    global FLAGS
    FLAGS="0000000000000000"
    return i+1

def n_ot(instr):
    reg1=reg[instr[10:13]]
    reg2=decimal(instr[13:])
    reg[reg1]=~reg2
    global FLAGS
    FLAGS="0000000000000000"
    return i+1

def c_mp(instr):
    global FLAGS
    reg1=reg[instr[10:13]]
    reg2=reg[instr[13:]]
    if reg1<reg2:
        FLAGS="0000000000000100"
    elif reg1>reg2:
        FLAGS="0000000000000010"
    else:
        FLAGS="0000000000000001"
    return i+1

def ld(instr):
    reg1=instr[6:9]
    mem = int( instr[9:] )
    loc = decimal( mem ) - l - 1  
    try:
        variables[ loc ]
    except:
        variables.append( 0 )
    # reg[reg1]=mem
    global FLAGS
    FLAGS="0000000000000000"
    return i+1

def st(instr):
    mem = int( instr[9:] )
    reg1=reg[instr[6:9]]
    loc = decimal( mem ) - l - 1 
    variables[ loc ] = reg1
    global FLAGS
    FLAGS="0000000000000000"
    return i+1

def jmp(instr):   # "01111"
    mem_addr = instr[10:]
    return decimal(mem_addr)
  
def jlt(instr):  # "11100"
    if FLAGS[14] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
    return i+1
      
def jgt(instr):  # "11101"
    if FLAGS[15] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
    return i+1
  
def je(instr):  # "11111"
    if FLAGS[16] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
    return i+1
      

def hlt():
    return 0

command_list=["0001000100000100", "0011100000001110", "1101000000000000"]


instructions = {"00010" : movImm
                , "00011" : mov_reg 
                , "00100" : ld 
                , "00101" : st
                , "00111" : div
                , "01000" : rs 
                , "01001" : ls
                , "01101" : n_ot  
                , "01110" : c_mp
                , "01111" : jmp
                , "11100" : jlt
                , "11101" : jgt
                , "11111" : je
                , "11010" : hlt()}

while ( command_list[i][:5]!='11010'):   #termination step is when we reach opcode of halt
    i=instructions[command_list[i][:5]](command_list[i])
    s=registers()
    print(binary(i,7)+"\n"+s+"\n\n")
