def check_instruction_A(instruction_list): # checks if instruction is of type A then returns 0
    if (len(instruction_list)==4) and (instruction_list[0] in command_A) and (instruction_list[1] in registers) and (instruction_list[2] in registers) and (instruction_list[3] in registers):
        return 0
    return 1
def check_instruction_B(instruction_list): # checks if instruction is of type B then returns 0
    try:
        int(instruction_list[2][1:])
    except:
        return 1
    if (len(instruction_list)==3) and (instruction_list[0] in command_B) and (instruction_list[1] in registers) and (0<=int(instruction_list[2][1:])<=127):
        return 0
    return 1
def check_instruction_C(instruction_list): # checks if instruction is of type C then returns 0
    if (len(instruction_list)==3) and (instruction_list[0] in command_C) and (instruction_list[1] in registers) and (instruction_list[2] in registers):
        return 0
    return 1
def check_instruction_D(instruction_list): # checks if instruction is of type D then returns 0
    if (len(instruction_list)==3) and (instruction_list[0] in command_D) and (instruction_list[1] in registers) and type(instruction_list[2]) == str:
        return 0
    return 1
def check_instruction_E(instruction_list): # checks if instruction is of type E then returns 0
    if (len(instruction_list)==2) and (instruction_list[0] in command_E) and type(instruction_list[1]) == str:
        return 0
    return 1
def check_instruction_F(instruction_list): # checks if instruction is of type F then returns 0
    if instruction_list==['hlt']:
        return 0
    return 1
def check_label(instruction_list): # checks if instruction is of type label the returns 0
                                   # i am assuming that the instructions are under the labels not in immediate continuation
    if instruction_list[0][-1] == ':' and len(instruction_list) == 1:
        return 0
    return 1

def check_variables(instruction_list):
    if instruction_list[0] == 'var' and len( instruction_list ) == 2 and type( instruction_list[1] == 'str'):
        return 0
    return 1

def check_flag( instruction_list ):
    if ['FLAGS'] in instruction_list and instruction_list[0] != 'mov':
        print(" invalid use of FLAGS register")
        return 0
    return 1

########## main ############

f=open("/home/mc/a.txt",'r')
command_list=f.readlines()
output=open("/home/mc/output_file.txt",'w')
for i in range(len(command_list)):
    command_list[i]=command_list[i].split()
print(command_list, '\n')
#will give the lines broken up into seperate words and gives empty lists for empty lines
######### start checking#########

l=len(command_list)
available_commands=['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']

command_A = ['add' , 'sub' , 'mul' , 'xor', 'or' , 'and']
command_B = ['mov' , 'rs' , 'ls']
command_C = ['mov' , 'not' , 'cmp' ]
command_D = ['ld' , 'st' ]
command_E = ['jmp' , 'jlt' , 'jgt', 'je']

registers=['R0','R1','R2','R3','R4','R5','R6','FLAGS']
label = []
######taking into account variables#######
lst, ind = [] , 0
for i in range(l):
    if not check_variables( command_list[i] ):         # assuming that after variable declaration length of instruction would not be 2
        lst.append(command_list[i][1])    # making variable list
        ind += 1
    elif command_list[i] == []:
        ind += 1
        continue
    else:
        break

for i in range(l):
    if not check_label( command_list[i] ):
        label.append( command_list[i][0][:len( command_list[i][0] )-1 ])
print( "labels are", label ,'\n' , "variables are " , lst , '\n')
for i in range(l): #starting to check for conditions

    if command_list[i]!=[]:
        ######checks for condition a ########

        if check_variables( command_list[i] ) and check_label( command_list[i] ) and check_instruction_A(command_list[i]) and  check_instruction_B(command_list[i]) and check_instruction_C(command_list[i]) and check_instruction_D(command_list[i]) and check_instruction_E(command_list[i]) and check_instruction_F(command_list[i]):
            #s = f"{i+1} incorrect instruction name or register name"
            print(i+1, "incorrect instruction name or register name")
            #f.write(s)
            continue

        ######checks for condition b #########

        if command_list[i][0] in {"ld","st"}:
            if command_list[i][2] not in lst:
                print("use of undefined variables")
                continue

        ###### checks for condition G #######

        if i>= ind and not check_variables( command_list[i] ):
            print("variables not defined at beginning")
            continue

        ######checks for condition e ########

        if not check_instruction_B(command_list[i]) and not(0<=int(command_list[i][2][1:])<=127):
            #s=f"{i+1} illegal immediate values"
            print(i+1, "illegal immediate values")
            #f.write(s)
            continue

        ######checks for condition c ########
        if not check_instruction_E( command_list[i] ) and command_list[i][1] not in label:
            print(command_list[i][1])
            #s=f"{i+1} use of undefined labels"
            print(i+1, " use of undefined labels")
            #f.write(s)
            continue

        ###### checks for condition F ########
        if not check_instruction_E( command_list[i] ) and  ( command_list[i][1][0 : len( command_list[i] )-1 ] in lst ):
            #s=f"{i+1} misuse variable as label "
            print(i+1," misuse variable as label")
            #f.write(s)
            continue


        if not check_instruction_D( command_list[i]) and ( command_list[i][2] not in lst ):
            #s=f"{i+1} misuse label as variable "
            print(i+1," misuse label as variable")
            #f.write(s)
            continue


        ##### checks for condition D#######

        if not check_flag( command_list [i] ):
            continue


######checks for condition H ########

if ['hlt'] not in command_list:
    #s=f'{l} hlt is missing'
    print(l,"hlt is missing")
    #f.write(s)

######checks for condition I ########

if ['hlt'] in command_list and ['hlt']!=command_list[l-1]:
    #s=f'{l} hlt is not last instruction'
    print(l," hlt is not last instruction")
    #f.write(s)

f.close()
output.close()
