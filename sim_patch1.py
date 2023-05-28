def globalisation():          # declares all variables as global
    global R0 , R1 , R2 , R3 , R4 , R5 , R6 , FLAGS
    return 
def registers():
    s = ''
    for i in reg:
        if i != "111":
            s += binary( reg[ i ] , 16 ) + ' ' #gives the output of the registers as binary 16 bits
    return s
def binary(x,n): #x->Decimal number, n->No of bits
    lst=["0" for i in range (n)]
    for i in range (n-1, -1, -1):
        lst[i]=str(x%2)
        x=x//2
    return "".join(lst)
def decimal(n): # converts from binary to decimal
    num, value , b = int( n ) , 0 , 1 
    tmp = num
    while( tmp != 0 ):
        l = tmp % 10
        tmp = tmp // 10
        value = value + l * base
        base *= 2
    return value
#----------------Your functions go here-------------

############## Main ##############

f=open("D:/Input.txt")
command_list = f.readlines()
len_of_command_list, i , R0 , R1 , R2 , R3 , R4 , R5 , R6 , FLAGS = len( command_list ) , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , '0000000000000000'
reg = { "000" : R0 , "001" : R1 , "010" : R2 , "011" : R3 , "100" : R4 , "101" : R5 , "110" : R6 , "111" : FLAGS }
instructions = { "00000" : add( reg[ command_list[i][7 : 10 ] ], reg[ command_list[i][ 10 : 13 ] ], reg[ command_list[i][ 13 : ] ] )
                , "00001" : sub( reg[ command_list[i][7 : 10 ] ] , reg[ command_list[i][ 10 : 13 ] ] , reg[ command_list[i][ 13 : ] ] )
                , "00010" : movImm( reg[ command_list[i][ 6 : 9 ] ] , decimal( command_list[i][ 9 : ] ) )
                , "00011" : mov_reg( reg[ command_list[i][10 : 13] ], reg[ command_list[i][ 13 : ] ] ) 
                , "00100" : ld( reg[ command_list[i][ 6 : 9 ] ] , command_list[i][ 9 : ] ) 
                , "00101" : st( reg[ command_list[i][ 6 : 9 ] ] , command_list[i][ 9 : ] )
                , "00111" : div( reg[ command_list[i][10 : 13] ], reg[ command_list[i][ 13 : ] ] ) 
                , "00110" : mul( reg[ command_list[i][7 : 10 ] ] , reg[ command_list[i][ 10 : 13 ] ], reg[ command_list[i][ 13 : ] ])
                , "01000" : rs( reg[ command_list[i][ 6 : 9 ] ] , decimal( command_list[i][ 9 : ] ) ) 
                , "01001" : ls( reg[ command_list[i][ 6 : 9 ] ] , decimal( command_list[i][ 9 : ] ) )
                , "01010" : xor( reg[ command_list[i][7 : 10 ] ] , reg[ command_list[i][ 10 : 13 ] ], reg[ command_list[i][ 13 : ] ] ) 
                , "01011" : o_r( reg[ command_list[i][7 : 10 ] ] , reg[ command_list[i][ 10 : 13 ] ] , reg[ command_list[i][ 13 : ] ] )
                , "01100" : a_nd( reg[ command_list[i][7 : 10 ] ] , reg[ command_list[i][ 10 : 13 ] ] , reg[ command_list[i][ 13 : ] ]) 
                , "01101" : n_ot( reg[ command_list[i][10 : 13] ], reg[ command_list[i][ 13 : ] ])  
                , "01110" : c_mp( reg[ command_list[i][10 : 13]] , reg[ command_list[i][ 13 : ] ]) 
                , "01111" : jmp( command_list[i][ 9 : ] ) 
                , "11100" : jlt( command_list[i][ 9 : ] ) 
                , "11101" : jgt( command_list[i][ 9 : ] ) 
                , "11111": je( command_list[i][ 9 : ] ) 
                , "11010" : hlt( command_list[i][ 10 : ] ) }
globalisation()
while ( command_list[ i ][ : 5 ] != '11010'):   #termination step is when we reach opcode of halt
    i = instructions[ command_list[i][ : 5] ]
    s = registers()
    print( binary( i , 7 ) + ' ' + s + ' ' + FLAGS )
f.close()
