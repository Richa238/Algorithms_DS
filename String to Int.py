def strtoint(s):
    res=0
    sign=1
    i=0
    if s[0]=='-':
        sign=-1
        i+=1
    for j in range (i,len(s)):
        res=res*10 + (ord(s[j])-ord('0'))

    out=res*sign
    print (out)


s = '-546'
strtoint(s)
