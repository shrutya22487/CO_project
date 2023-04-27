def Decimel_to_binary(num):             // code to convert decimel to binary
    bin_num = ""
    if num == 0:
        bin_num = "0"
    else:
        while num > 0:
            bin_num = str( num % 2 ) + bin_num
            num = num // 2
    return bin_num
