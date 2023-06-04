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
l = ['D:\\test1.txt', 'D:\\test2.txt', 'D:\\test3.txt', 'D:\\test4.txt', 
    'D:\\test5.txt' ]
for file in l:
    f = open(file)
    command_list = f.readlines()
    l = len(command_list)
    for i in range(l):
        command_list[i] = command_list[i].strip()
    
    variables = []

    def decimal(n): # converts from binary to decimal
        num, value , base = int( n ) , 0 , 1 
        tmp = num
        while( tmp != 0 ):
            l = tmp % 10
            tmp = tmp // 10
            value = value + l * base
            base *= 2
        return value
    
    def decf_simulator(instr):
        source_reg = reg[instr[10:13] ]
        dest_reg = instr[13:16]
        reg[dest_reg] = source_reg - 1
        return i + 1
    
    def decf_assembly(source_reg,dest_reg):
        machinecode = "1000000000" + source_reg + dest_reg + "\n"
        print(machinecode)

    def incf_simulator(instr):
        source_reg = reg[instr[10:13] ]
        dest_reg = instr[13:16]
        reg[dest_reg] = source_reg - 1
        return i + 1
    
    def incf_assembly(source_reg,dest_reg):
        machinecode = "1000010000" + source_reg + dest_reg + "\n"
        print(machinecode)
    
    def comf_simulator(instr):
        source_reg = str(reg[instr[10:13] ])
        s = ''
        for ch in source_reg:
            if ch == '1':
                s += '0'
            else:
                s += '1'
        dest_reg = instr[13:16]
        reg[dest_reg] = int(s)
        return i + 1

    def comf_assembly(source_reg,dest_reg):
        machinecode = "1000100000" + source_reg + dest_reg + "\n"
        print(machinecode)

    def jmp(instr):   # "01111"
        mem_addr = instr[10:]
        reg["111"]=0
        return decimal(mem_addr)
    
    def decfz_simulator(instr):
        reg1 = reg[instr[6:9]]
        reg[reg1] = reg1 - 1
        mem_addr = instr[10:]
        reg["111"]=0
        if reg[reg1] == 0:   
            return decimal(mem_addr)
        else:
            return i + 1
    
    def decfz_assembly(source_reg,mem_address):
        machinecode = "1000110" + source_reg + mem_address + "\n"
        print(machinecode)

    def incfz_simulator(instr):
        reg1 = reg[instr[6:9]]
        reg[reg1] = reg1 + 1
        mem_addr = instr[10:]
        reg["111"]=0
        if reg[reg1] == 0:
            return decimal(mem_addr)
        else:
            return i + 1
    
    def incfz_assembly(source_reg,mem_address):
        machinecode = "1001000" + source_reg + mem_address + "\n"
        print(machinecode)

opcode = {"decf": "100000","incf": "100001","comf": "100010","swapf": "100011","decf": "100000"}
registers_dict = {"R0": "000", "R1": "001", "R2": "010","R3": "011","R4": "100","R5": "101","R6": "110"}
for instr in command_list: 
    if instr != []:
        op=instr[0]
        if op == "decf":
            decf_assembly(registers_dict.get(instr[1]),registers_dict.get(instr[2]))
        elif op == "incf":
            incf_assembly(registers_dict.get(instr[1]),registers_dict.get(instr[2]))
        elif op == "mul":
            comf_assembly(registers_dict.get(instr[1]),registers_dict.get(instr[2]))
        elif op == "xor":
            decfz_assembly(registers_dict.get(instr[1]),registers_dict.get(instr[2]))
        elif op == "or":
            incfz_assembly(registers_dict.get(instr[1]),registers_dict.get(instr[2]))
