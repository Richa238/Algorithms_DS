def int_to_str(num):
    if num<0:
        num, sign=-num,True
    res=[]
    while True:
        res.append(chr(ord('0')+(num%10)))
        num//=10
        if num==0:
            break
    print( ('-' if sign else '')+''.join(reversed(res)))
n=-341
int_to_str(n)