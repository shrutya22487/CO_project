def movImm(reg1,val):
    reg1=val
    FLAGS="0000000000000000"
    return i+1

def mov_reg(reg1, reg2):
    reg1=reg2
    FLAGS="0000000000000000"
    return i+1

def div(reg3, reg4):
    if reg4==0:
        FALGS="0000000000001000"
        R0, R1=0,0
        return i+1
    R0=reg3//reg4
    R1=reg3%reg4
    FLAGS="0000000000000000"
    return i+1

def rs(reg1, val):
    reg1=reg1>>val
    FLAGS="0000000000000000"
    return i+1

def ls(reg1, val):
    reg1=reg1<<val
    FLAGS="0000000000000000"
    return i+1

def n_ot(reg1, reg2):
    reg1=~reg2
    FLAGS="0000000000000000"
    return i+1

def c_mp(reg1, reg2):
    if reg1<reg2:
        FLAGS="0000000000000100"
    elif reg1>reg2:
        FALGS="0000000000000010"
    else:
        FLAGS="0000000000000001"
    return i+1

def ld(reg1, mem):
    reg1=mem
    FLAGS="0000000000000000"
    return i+1

def st(reg1, mem):
    mem=reg1
    FLAGS="0000000000000000"
    return i+1

def hlt():
    return 0
