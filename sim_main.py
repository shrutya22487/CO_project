i , R0 , R1 , R2 , R3 , R4 , R5 , R6 , FLAGS =0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , [0 for k in range (16)]
reg = { "000" : R0 , "001" : R1 , "010" : R2 , "011" : R3 , "100" : R4 , "101" : R5 , "110" : R6 , "111" : FLAGS }  
l = ['D:\\test1.txt', 'D:\\test2.txt', 'D:\\test3.txt', 'D:\\test4.txt', 
     'D:\\test5.txt' ]
#f =open("D:\\test1.txt")

for i in l:
    f = open( i )
    command_list = f.readlines()
    l = len ( command_list )
    for i in range( l ):
        command_list[i] = command_list[i].split("\n")
    
    variables = [] 
    def registers():
        global FLAGS
        s=''
        for j in reg:
            if j!="111":
                s+=binary(reg[j],16) + '\n' #gives the output of the registers as binary 16 bits
        FLAGS=list(map(str, FLAGS))
        s+="".join(FLAGS)
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
        global FLAGS
        reg2= reg[instr[10:13]]
        reg3= reg[instr[13:]]
        reg1=instr[7:10]
        reg[reg1]= reg2 + reg3
        if reg[reg1] > (2**16 -1) or reg[reg1] < -(2**16):
            FLAGS[12]=1
            reg[reg1] = binary(0,16)
        else:
            FLAGS=[0 for k in range (16)]
        
        return i+1

    def sub(instr):
        global FLAGS
        reg2=reg[instr[10:13]]
        reg3=reg[instr[13:]]
        reg1=instr[7:10]
        reg[reg1] = reg2 - reg3
        if reg[reg2] < reg[reg3]:
            FLAGS[12]=1
            reg[reg1] = binary(0,16)
        else:
            FLAGS=[0 for k in range (16)]
        
        return i+1

    def mul(instr):
        global FLAGS
        reg2= reg[instr[10:13]]
        reg3= reg[instr[13:]]
        reg1=instr[7:10]
        reg[reg1]= reg2 * reg3
        if reg[reg1] > (2**16 -1) or reg[reg1] < -(2**16):
            FLAGS[12]=1
            reg[reg1] = binary(0,16)
        else:
            FLAGS=[0 for k in range (16)]
        
        return i+1

    def bit_xor(instr):
        global FLAGS
        reg2=reg[instr[10:13]]
        reg3=reg[instr[13:]]
        reg1=instr[7:10]
        reg[reg1] = reg2 ^ reg3
        FLAGS=[0 for k in range (16)]
        return i+1

    def bit_or(instr):
        global FLAGS
        reg2=reg[instr[10:13]]
        reg3=reg[instr[13:]]
        reg1=instr[7:10]
        reg[reg1] = reg2 | reg3
        FLAGS=[0 for k in range (16)]
        return i+1

    def bit_and(instr):
        global FLAGS
        reg2=reg[instr[10:13]]
        reg3=reg[instr[13:]]
        reg1=instr[7:10]
        reg[reg1] = reg2 & reg3
        FLAGS=[0 for k in range (16)]
        return i+1

    def movImm(instr):
        global FLAGS
        reg1=instr[6:9]
        val=decimal(instr[9:])
        reg[reg1]=val
        FLAGS=[0 for k in range (16)]
        return i+1

    def mov_reg(instr):
        global FLAGS
        reg1=instr[10:13]
        reg2=reg[instr[13:]]
        reg[reg1]=reg2
        FLAGS=[0 for k in range (16)]
        return i+1

    def div(instr):
        global FLAGS
        reg3=reg[instr[10:13]]
        reg4=reg[instr[13:]]
        if reg4==0:
            FLAGS[12]=1
            reg["000"]=0
            reg["001"]=0
            return i+1
        reg["000"]=reg3//reg4
        reg["001"]=reg3%reg4
        FLAGS=[0 for k in range (16)]
        return i+1

    def rs(instr):
        global FLAGS
        reg1=instr[6:9]
        val=decimal(instr[9:])
        reg[reg1]=reg[reg1]>>val
        FLAGS=[0 for k in range (16)]
        return i+1

    def ls(instr):
        global FLAGS
        reg1=instr[6:9]
        val=decimal(instr[9:])
        reg[reg1]=reg[reg1]<<val
        FLAGS=[0 for k in range (16)]
        return i+1

    def n_ot(instr):
        global FLAGS
        reg1=reg[instr[10:13]]
        reg2=decimal(instr[13:])
        reg[reg1]=~reg2
        FLAGS=[0 for k in range (16)]
        return i+1

    def c_mp(instr):
        global FLAGS
        reg1=reg[instr[10:13]]
        reg2=reg[instr[13:]]
        if reg1<reg2:
            FLAGS[13]=1
        elif reg1>reg2:
            FLAGS[14]=1
        else:
            FLAGS[15]=1
        return i+1

    def ld(instr):
        global FLAGS
        reg1=instr[6:9]
        mem = int( instr[9:] )
        loc = decimal( mem ) - l + 1  
        try:
            variables[loc]
        except:
            variables.append( 0 )
        reg[reg1]=variables[loc] #Review this
        FLAGS=[0 for k in range (16)]
        return i+1

    def st(instr):
        global FLAGS
        mem = int( instr[9:] )
        reg1 = reg[ instr[6:9] ]
        loc = decimal( mem ) - l + 1 
        variables[ loc ] = reg1
        FLAGS=[0 for k in range (16)]
        return i+1

    def jmp(instr):   # "01111"
        global FLAGS
        mem_addr = instr[10:]
        FLAGS=[0 for k in range (16)]
        return decimal(mem_addr)
    
    def jlt(instr):  # "11100"
        global FLAGS
        if FLAGS[13] == 1:
            mem_addr = instr[10:]
            return decimal(mem_addr)
        FLAGS=[0 for k in range (16)]
        return decimal(mem_addr)
        
    def jgt(instr):  # "11101"
        global FLAGS
        if FLAGS[14] == 1:
            mem_addr = instr[10:]
            return decimal(mem_addr)
        FLAGS=[0 for k in range (16)]
        return decimal(mem_addr)
    
    def je(instr):  # "11111"
        global FLAGS
        if FLAGS[15] == 1:
            mem_addr = instr[10:]
            return decimal(mem_addr)
        FLAGS=[0 for k in range (16)]
        return decimal(mem_addr)

    def hlt():
        return 0
    def memory_dump():
        for i in command_list:
            print( '000000000' + i )
        for i in range( l , 129 ):
            print( '0000000000000000' )

    instructions = { "00000" : add
                    , "00001" : sub
                    , "00010" : movImm
                    , "00011" : mov_reg 
                    , "00100" : ld 
                    , "00101" : st
                    , "00110" : mul
                    , "00111" : div
                    , "01000" : rs 
                    , "01001" : ls
                    , "01010" : bit_xor
                    , "01011" : bit_or
                    , "01100" : bit_and
                    , "01101" : n_ot  
                    , "01110" : c_mp
                    , "01111" : jmp
                    , "11100" : jlt
                    , "11101" : jgt
                    , "11111" : je
                    , "11010" : hlt}
    i = 0
    while ( command_list[i][:5]!='11010'):   #termination step is when we reach opcode of halt
        i=instructions[command_list[i][:5]](command_list[i])
        s=registers()
        print(binary(i,7)+" "+s+" ")
    memory_dump()
    print("\n")
    f.close()
