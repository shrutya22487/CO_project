import sys
label_num = 0
def check_instruction_A(instruction_list): # checks if instruction is of type A then returns 0
    if len(instruction_list)==4 :
        if (instruction_list[0] in command_A) and (instruction_list[1] in registers) and (instruction_list[2] in registers) and (instruction_list[3] in registers):
            return 0
    return 1
def check_instruction_B(instruction_list): # checks if instruction is of type B then returns 0
    try:
        int(instruction_list[2][1:])
    except:
        return 1
    if len(instruction_list)==3 :
        if (instruction_list[0] in command_B) and (instruction_list[1] in registers and instruction_list[2][0] == '$') :
            return 0
    #print("CHECK")
    return 1
def check_instruction_C(instruction_list): # checks if instruction is of type C then returns 0
    if len(instruction_list)==3:
        if  (instruction_list[0] in command_C) and (instruction_list[1] in registers) and (instruction_list[2] in registers):
            return 0
    return 1
def check_instruction_D(instruction_list): # checks if instruction is of type D then returns 0
    
    if len( instruction_list ) == 3:
        if (instruction_list[0] in command_D) and (instruction_list[1] in registers) and type(instruction_list[2]) == str :
           # print("check")
            #print(instruction_list)
            return 0
    return 1
def check_instruction_E(instruction_list): # checks if instruction is of type E then returns 0
    if len(instruction_list)==2:
        if (instruction_list[0] in command_E) and type(instruction_list[1]) == str:
            return 0
    return 1
def check_instruction_F(instruction_list): # checks if instruction is of type F then returns 0
    if instruction_list==['hlt']:
        return 0
    return 1
def check_label(instruction_list): # checks if instruction is of type label the returns 0
    if instruction_list[0][-1] == ':' :
        return 0
    return 1

def check_variables(instruction_list):
    if len( instruction_list ) == 2:
        if instruction_list[0] == 'var' and type( instruction_list[1] == str):
            return 0
    return 1

def check_flag( instruction_list ):
    if 'FLAGS' in instruction_list and instruction_list[0] != 'mov':
        print(" invalid use of FLAGS register")
        return 0
    return 1

def binary(x,n):
    lst=["0" for i in range (n)]
    for i in range (n-1, -1, -1):
        lst[i]=str(x%2)
        x=x//2
    return "".join(lst)

def movImm(lst): #00010 mov
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print("00010"+"0"+r+val+"\n")
def rightShift(lst): #01000 rs
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print("01000"+"0"+r+val+"\n")
def leftShift(lst): #01001 ls
    r=binary(int(lst[1][-1]),3)
    val=binary(int(lst[2][1:]),7)
    print("01001"+"0"+r+val+"\n")

def movReg(lst): #00011 mov
    if lst[1]=='FLAGS' and lst[2]!='FLAGS':
        reg1=binary(7,3)
        reg2=binary(int(lst[2][-1]),3)
    elif lst[1]!='FLAGS' and lst[2]=='FLAGS':
        reg1=binary(int(lst[1][-1]),3)
        reg2=binary(7,3)
    else:
        reg1=binary(int(lst[1][-1]),3)
        reg2=binary(int(lst[2][-1]),3)
    print("00011"+"00000"+reg1+reg2+"\n")
def divide(lst): #00111 div
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print("00111"+"00000"+reg1+reg2+"\n")
def invert(lst): #01101 not
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print("01101"+"00000"+reg1+reg2+"\n")
def compare(lst): #01110 cmp
    reg1=binary(int(lst[1][-1]),3)
    reg2=binary(int(lst[2][-1]),3)
    print("01110"+"00000"+reg1+reg2+"\n")

def load(lst, addr): #00100 ld
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr, 7)
    print("00100"+"0"+r+addr+"\n")
def store(lst, addr): #00101 st
    r=binary(int(lst[1][-1]),3)
    addr=binary(addr,7)
    print("00101"+"0"+r+addr+"\n")

def jmp(lst,code,var_lst):   # "01111"
    label_num1 = 0
    for i in range(len(var_lst),len(code)):
        if lst[1] == code[i][0][:-1]:
            break
    for j in range(i):
        if not check_label(code[j]):
            label_num1 += 1 
    val = binary(i-len(var_lst)-label_num1,7)
    print("01111"+"0000"+val+"\n")

def jlt(lst,code,var_lst):  # "11100"
    label_num1 = 0
    for i in range(len(var_lst),len(code)):
        if lst[1] == code[i][0][:-1]:
            break
    for j in range(i):
        if not check_label(code[j]):
            label_num1 += 1
    val = binary(i-len(var_lst)-label_num1,7)
    print("11100"+"0000"+val+"\n")
            
def jgt(lst,code,var_lst):  # "11101"
    label_num1 = 0
    for i in range(len(var_lst),len(code)):
        if lst[1] == code[i][0][:-1]:
            break
    for j in range(i):
        if not check_label(code[j]):
            label_num1 += 1
    val = binary(i-len(var_lst)-label_num1,7)
    print("11101"+"0000"+val+"\n")
            
def je(lst,code,var_lst):  # "11111"
    label_num1 = 0
    for i in range(len(var_lst),len(code)):
        if lst[1] == code[i][0][:-1]:
            break
    for j in range(i):
        if not check_label(code[j]):
            label_num1 += 1
    val = binary(i-len(var_lst)-label_num1,7)
    print("11111"+"0000"+val+"\n")
            

def halt(): #11010 hlt
    print("11010"+"00000000000"+"\n")
    
def add(x,y,z):
    machinecode = "0000000" + x + y + z+"\n"
    print(machinecode)
def sub(x,y,z):
    machinecode = "0000100" + x + y + z+"\n"
    print(machinecode)
def mul(x,y,z):
    machinecode = "0011000" + x + y + z+"\n"
    print(machinecode)
def xor(x,y,z):
    machinecode = "0101000" + x + y + z+"\n"
    print(machinecode)
def orfunc(x,y,z):
    machinecode = "0101100" + x + y + z+"\n"
    print(machinecode)
def andfunc(x,y,z):
    machinecode = "0110000" + x + y + z+"\n"
    print(machinecode)

########## main ############

command_list = sys.stdin.readlines()
#command_list = input.readlines()
#f=open("output.txt",'w')
for i in range(len(command_list)):
    command_list[i]=command_list[i].split()
#print(command_list, '\n')
#will give the lines broken up into seperate words and gives empty lists for empty lines
######### start checking#########


available_commands = ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']

command_A = ['add' , 'sub' , 'mul' , 'xor', 'or' , 'and']
command_B = ['mov' , 'rs' , 'ls']
command_C = ['mov' , 'div' , 'not' , 'cmp' ]
command_D = ['ld' , 'st' ]
command_E = ['jmp' , 'jlt' , 'jgt', 'je']

registers=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
label = []
######taking into account variables#######
lst, ind = [] , 0
flag = 0

for i, instr in enumerate(command_list):
    if not check_label(instr):
        label.append(instr[0][:len(instr[0])-1])
        next_instr = instr[1:]
        command_list[i] = [instr[0]]
        command_list.insert(i + 1, next_instr)


#print (command_list)

l=len( command_list )

for i in range(l):
    if command_list[i] == []:         # assuming that after variable declaration length of instruction would not be 2
        ind += 1
        continue
    elif not check_variables( command_list[i] ):
        #print( command_list[i] )
        lst.append(command_list[i][1])    # making variable list
        ind += 1
    else:
        break



#print( "labels are", label ,'\n' , "variables are " , lst , '\n')
for i in range(l): #starting to check for conditions 
    if command_list[i]!=[]:
        ######checks for condition a ########

        if check_variables( command_list[i] ) and check_label( command_list[i] ) and check_instruction_A(command_list[i]) and  check_instruction_B(command_list[i]) and check_instruction_C(command_list[i]) and check_instruction_D(command_list[i]) and check_instruction_E(command_list[i]) and check_instruction_F(command_list[i]):
            flag += 1
            s = f"Error in line {i+1-label_num}: incorrect instruction name or register name\n"
            print(s)
            #print(s)
            continue   # change f as output in file
        if not check_instruction_D( command_list[i]) and ( command_list[i][2] not in lst ):
            if command_list[i][2]  in label:
                flag += 1
                s=f"Error in line {i+1-label_num}: misuse of label as variable\n "
                print(s)
                #print(s)
                continue 
        ######checks for condition b #########

        if command_list[i][0] in {"ld","st"}:
            if command_list[i][2] not in lst:
                flag += 1
                s = f"Error in line {i+1-label_num}: use of undefined variables\n"
                print(s)
                #print(s)
                continue

        ###### checks for condition G #######

        if i>= ind and not check_variables( command_list[i] ):
            flag += 1
            s = f"Error in line {i+1-label_num}: variables not defined at beginning \n"
            #print(i + 1 , "variables not defined at beginning")
            print(s)
            continue

        ######checks for condition e ########

        if not check_instruction_B(command_list[i]) and not(0<=int(command_list[i][2][1:])<=127):
            flag += 1
            s=f"Error in line {i+1-label_num}: illegal immediate values\n"
            #print(i+1, "illegal immediate values")
            print(s)
            continue

        ######checks for condition c ########
        if not check_instruction_E( command_list[i] ) and command_list[i][1] not in label:
            flag += 1
            #print(command_list[i][1])
            s=f"Error in line {i+1-label_num}: use of undefined labels\n"
            #print(i+1, " use of undefined labels")
            print(s)
            continue

        ###### checks for condition F ########
        if not check_instruction_E( command_list[i] ) and  ( command_list[i][1] in lst ):
            flag += 1
            s=f"Error in line {i+1-label_num}: misuse variable as label \n"
            #print(i+1," misuse variable as label")
            print(s)
            continue

        ##### checks for condition D#######

        if 'FLAGS' in command_list[ i ] and command_list[ i ][0] != 'mov':
            flag += 1
            s=f"Error in line {i+1-label_num}: illegal use of FLAGS\n "
            print(s)
            continue


######checks for condition H ########

        if ['hlt'] not in command_list:
            flag += 1
            s=f'Error in line {l}: hlt is missing'
            #print(l,"hlt is missing")
            print(s)
            break

######checks for condition I ########

        if ['hlt'] in command_list and ['hlt'] != command_list[-1]:
            flag += 1
            s=f'Error in line {l}: hlt is not last instruction'
            #print(l," hlt is not last instruction")
            print(s)
            break
   
registers_dict = {"R0": "000", "R1": "001", "R2": "010","R3": "011","R4": "100","R5": "101","R6": "110"}
addr=l-1-len(label)-len(lst)
if (not flag):
    for instr in command_list: 
        if instr != []:
            op=instr[0]
            if op=="mov":
                if ("$" in instr[2]):
                    movImm(instr)
                else:
                    movReg(instr)
            elif op == "add":
                add(registers_dict.get(instr[1]),registers_dict.get(instr[2]),registers_dict.get(instr[3]))
            elif op == "sub":
                sub(registers_dict.get(instr[1]),registers_dict.get(instr[2]),registers_dict.get(instr[3]))
            elif op == "mul":
                mul(registers_dict.get(instr[1]),registers_dict.get(instr[2]),registers_dict.get(instr[3]))
            elif op == "xor":
                xor(registers_dict.get(instr[1]),registers_dict.get(instr[2]),registers_dict.get(instr[3]))
            elif op == "or":
                orfunc(registers_dict.get(instr[1]),registers_dict.get(instr[2]),registers_dict.get(instr[3]))
            elif op == "and":
                andfunc(registers_dict.get(instr[1]),registers_dict.get(instr[2]),registers_dict.get(instr[3]))
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
                jmp(instr,command_list,lst)
            elif op == "jlt":
                jlt(instr,command_list,lst)
            elif op == "je":
                je(instr,command_list,lst)
            elif op=="jgt":
                jgt(instr,command_list,lst)
            elif op=="hlt":
                halt()

#f.close()
#input.close()
