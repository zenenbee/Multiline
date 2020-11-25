with open('code.mutl','r') as f:

    cod = f.readlines()

counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count = 5
cursor = 51
looppoints = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
clen = len(cod)
part = 0
countstack = ""

def use(code):
    global counts
    global part
    global countstack
    global cursor
    global count
    global clen
    if cursor > 100 or cursor < 0:
        print(code)
        print("Cursor outside of range on line "+str(part+1))
        print("Cursor value: "+str(cursor))
        part = clen + 1
    else:
        count = counts[cursor]

    if code.startswith('print('):     
        if code.replace('\n','').endswith(')'):
            exec(code)
        else:
            print(code)
            print("Code outside of print function on "+str(part+1))

    if code.startswith('printcount()'):
        print(chr(count))

    if code.startswith('pushstack()'):
        countstack += chr(count)

    if code.startswith('readstack()'):
        print(countstack)





    if code.startswith('count('):
        counts[cursor] += int(code.replace('count(','',1).replace(')','',1))

    if code.startswith('cursor('):
        cursor += int(code.replace('cursor(','',1).replace(')','',1))

    if code.startswith('[Loop]'):
        global looppoints

        id = int(code.replace('[Loop] ','',1))

        if looppoints[id] == -1:
            looppoints[id] = part
        else:
            if count != 0:
                part = looppoints[id]
            else:
                looppoints[id] = -1



while part < clen:
    use(cod[part])
    part += 1