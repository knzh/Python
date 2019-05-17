import math
def quadratic(a,b,c):
    m=b*b-4*a*c
    n=math.sqrt(m)
    if n>=0:
        s=-(b-n)/2*a
        d=-(b+n)/2*a
        return s,d
    else:
        pass
print(quadratic(1,2,1))
