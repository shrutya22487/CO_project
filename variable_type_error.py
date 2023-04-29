def use_of_undefined_variables(code):
    lst = []
    for i in range(len(code)):
        if len(code[i]) == 2:         # assuming that after variable declaration length of instruction would not be 2
            lst.append(code[i][1])    # making variable list
        else:
            break
    for j in range(i,len(code)):
        if code[j][0] in {"ld","st"}:
            if code[j][2] not in lst:
                print("syntax error")
                break

def variables_not_defined_at_begin(code):
    for i in range(len(code)):
        if len(code[i]) != 2:
            break
    for j in range(i,len(code)):
        if code[j][0] == "var":
            print("syntax error")
            break
