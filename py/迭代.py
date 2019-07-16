'''

for i,j in enumerate(['a','b','v','e']):
    print(i,j)
    
'''

'''
for x,y in [(1,2),(3,4),(5,6),('a','b')]:
    print(x,y)

'''

'''
def find(L):
    max=min=L[0]
    for i in L:
        if i<max:
            max=max;
        else:
            max=i;
    for j in L:
        if j<min:
            min=j;
        else:
            min=min;
    print(min,max)

find([3,4,6,7,8,1,231])
'''

'''
def find(L):
    while L:
        max=min=L[0]
        for i in L:
            if i>max:
                max=i;
            elif i<min:
                min=i;
        return(min,max)
    return(None,None)

find([3,4,6,7,8,1,231])
'''
