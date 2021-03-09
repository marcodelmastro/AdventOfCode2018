def addr(a,b,c,reg):
    '''(add register) stores into register C the result of adding register A and register B.'''
    reg[c] = reg[a] + reg[b]
    return reg

def addi(a,b,c,reg):
    '''(add immediate) stores into register C the result of adding register A and value B.'''
    reg[c] = reg[a] + b
    return reg

def mulr(a,b,c,reg):
    '''(multiply register) stores into register C the result of multiplying register A and register B.'''
    reg[c] = reg[a] * reg[b]
    return reg
    
def muli(a,b,c,reg):
    '''muli (multiply immediate) stores into register C the result of multiplying register A and value B.'''
    reg[c] = reg[a] * b
    return reg

def banr(a,b,c,reg):
    '''(bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.'''
    reg[c] = reg[a] & reg[b]
    return reg

def bani(a,b,c,reg):
    '''(bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.'''
    reg[c] = reg[a] & b
    return reg
    
def borr(a,b,c,reg):
    ''' (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.'''
    reg[c] = reg[a] | reg[b]
    return reg

def bori(a,b,c,reg):
    ''' (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.'''
    reg[c] = reg[a] | b
    return reg

def setr(a,b,c,reg):
    ''' (set register) copies the contents of register A into register C. (Input B is ignored.)'''
    reg[c] = reg[a]
    return reg
    
def seti(a,b,c,reg):
    ''' (set immediate) stores value A into register C. (Input B is ignored.)'''
    reg[c] = a
    return reg

def gtir(a,b,c,reg):
    ''' (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.'''
    if a>reg[b]:
        reg[c]=1
    else:
        reg[c]=0
    return reg
    
def gtri(a,b,c,reg):
    ''' (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.'''
    if reg[a]>b:
        reg[c]=1
    else:
        reg[c]=0
    return reg

def gtrr(a,b,c,reg):
    ''' (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.'''
    if reg[a]>reg[b]:
        reg[c]=1
    else:
        reg[c]=0
    return reg
    
def eqir (a,b,c,reg):
    '''(equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.'''
    if a==reg[b]:
        reg[c]=1
    else:
        reg[c]=0
    return reg

def eqri(a,b,c,reg):
    ''' (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.'''
    if reg[a]==b:
        reg[c]=1
    else:
        reg[c]=0
    return reg

def eqrr(a,b,c,reg):
    ''' (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.'''
    if reg[a]==reg[b]:
        reg[c]=1
    else:
        reg[c]=0
    return reg


def getProg(filename):
    with open(filename) as f:
        lines = [ l.strip("\n") for l in f.readlines()  ]
    ip = -1
    prog = []
    for l in lines:
        if l.split(" ")[0]=="#ip":
            ip = int(l.split(" ")[1])
        else:
            op = l.split(" ")[0]
            v = [ int(b) for b in l.split(" ")[1:] ]
            p = [op]
            p+=v
            prog.append(p)
    return ip, prog


def getProg(filename):
    with open(filename) as f:
        lines = [ l.strip("\n") for l in f.readlines()  ]
    ip = -1
    prog = []
    for l in lines:
        if l.split(" ")[0]=="#ip":
            ip = int(l.split(" ")[1])
        else:
            op = l.split(" ")[0]
            v = [ int(b) for b in l.split(" ")[1:] ]
            p = [op]
            p+=v
            prog.append(p)
    return ip, prog


def executeProg(ipr,prog,r0=0,verbose=False,stopAfter=-1): 

    #from AOC2018 import addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr

    reg = [r0,0,0,0,0,0]
    ip = 0 # The instruction pointer starts at 0
    
    it = 0
    while True:
    
        reg[ipr] = ip
        
        if verbose: 
            print(ip,reg,prog[ip],end=" ")

        op,a,b,c = prog[ip]
        
        if   op=='addr': reg = addr(a,b,c,reg)
        elif op=='addi': reg = addi(a,b,c,reg)
        elif op=='mulr': reg = mulr(a,b,c,reg)
        elif op=='muli': reg = muli(a,b,c,reg)
        elif op=='banr': reg = banr(a,b,c,reg)
        elif op=='bani': reg = bani(a,b,c,reg)
        elif op=='borr': reg = borr(a,b,c,reg)
        elif op=='bori': reg = bori(a,b,c,reg)
        elif op=='setr': reg = setr(a,b,c,reg)
        elif op=='seti': reg = seti(a,b,c,reg)
        elif op=='gtir': reg = gtir(a,b,c,reg)
        elif op=='gtri': reg = gtri(a,b,c,reg)
        elif op=='gtrr': reg = gtrr(a,b,c,reg)
        elif op=='eqir': reg = eqir(a,b,c,reg)
        elif op=='eqri': reg = eqri(a,b,c,reg)
        elif op=='eqrr': reg = eqrr(a,b,c,reg) 

        if verbose: print(reg)

        ip = reg[ipr]
        ip+=1

        if ip>=len(prog):
            break
            
        it+=1
        if stopAfter>0 and it>=stopAfter:
            break

    return reg
