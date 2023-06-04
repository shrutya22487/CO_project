i , R0 , R1 , R2 , R3 , R4 , R5 , R6 , FLAGS =0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , [0 for k in range (16)]
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
for file in l:
    f = open(file)
    command_list = f.readlines()
    l = len(command_list)
    for i in range(l):
        command_list[i] = command_list[i].strip()
    
    variables = []

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

    def float_bin(f_no):
        f_str = str(f_no)
        ind = f_str.index('.')
        exp = ind -1
        bias = 3
        bias_exp = bias + exp
        s = ''
        for ch in f_str:
            if ch.isdigit():
                s += ch
        mantissa = s[1:]
        bias_exp = binary(bias_exp,3)
        mantissa = binary(mantissa,5)
        number = bias_exp + mantissa
        number = int(number)
        return number

    def float_dec(d_no):
        d_str = str(d_no)
        exp_bias = d_str[0:3]
        exp_bias = decimal(int(exp_bias))
        exp = exp_bias - 3
        mantissa = decimal(int(d_str[3:]))
        p = decimal(float("1." + d_str[3:]))
        number = p * (10**exp)
        return number


    def overflow(f_no,dec_no):
        f_str = str(f_no)
        ind = f_str.index('.')
        exp = ind -1
        bias = 3
        bias_exp = bias + exp
        s = ''
        for ch in f_str:
            if ch.isdigit():
                s += ch
        mantissa = s[1:]
        if bias_exp > 7 and mantissa >= 0:
            FLAGS[12]=1
            dec_no = 0
        else:
            FLAGS=[0 for k in range (16)]
        return FLAGS, dec_no
            

    def addf(instr):
        global FLAGS
        reg2= reg[instr[10:13] ]
        reg3= reg[instr[13:16] ]
        reg1=instr[7:10]
        reg[reg1]= reg2 + reg3
        decimal = reg2 + reg3
        FLAGS,reg[reg1] = overflow(decimal,reg[reg1])
        return i+1

    def subf(instr):
        global FLAGS
        reg2 = reg[instr[10:13]]
        reg3 = reg[instr[13:]]
        reg1 = instr[7:10]
        reg[reg1] = reg2 - reg3
        if reg2 < reg3:
            FLAGS[12] = 1
            reg[reg1] = 0
        else:
            FLAGS = [0 for k in range(16)]

        return i + 1

    def movfImm(instr):
        global FLAGS
        reg1=instr[6:9]
        val = float_dec(instr[9:])
        reg[reg1]=val
        FLAGS=[0 for k in range (16)]
        return i+1