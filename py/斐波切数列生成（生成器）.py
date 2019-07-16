def bfq(max):
    x,a,b=0,0,1
    while x<max:
        print(b)
        a,b=b,a+b
        x+=1
    return'done'
bfq(10)