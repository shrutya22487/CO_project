def jmp(instr):   # "01111"
    mem_addr = instr[10:]
    return decimal(mem_addr)
  
def jlt(instr):  # "11100"
    if FLAGS[14] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
      
def jgt(instr):  # "11101"
    if FLAGS[15] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
  
def je(instr):  # "11111"
    if FLAGS[16] == "1":
        mem_addr = instr[10:]
        return decimal(mem_addr)
      
      
instructions = {"00010" : movImm
                , "00011" : mov_reg 
                , "00100" : ld 
                , "00101" : st
                , "00111" : div
                , "01000" : rs 
                , "01001" : ls
                , "01101" : n_ot  
                , "01110" : c_mp
                , "01111" : jmp
                , "11100" : jlt
                , "11101" : jgt
                , "11111" : je
                , "11010" : hlt()}
