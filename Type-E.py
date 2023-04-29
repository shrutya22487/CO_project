def jmp(lst,code):   # "01111"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            print("01111","0000",binary(i,7))
            break

def jlt(lst,code,flag):  # "11100"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag < 1:
                print("11100","0000",binary(i,7))
                break
            break

def jgt(lst,code,flag):  # "11101"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag > 1:
                print("11101","0000",binary(i,7))
                break
            break

def je(lst,code,flag):  # "11111"
    for i in range(len(code)):
        if lst[1] == code[i][0]:
            if flag == 1:
                print("11111","0000",binary(i,7))
                break
            break
