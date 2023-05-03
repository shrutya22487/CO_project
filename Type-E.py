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
