'''

L=[]
for x in range(0,20):
    L.append(x*x)

print(L)
'''


'''
L=[x*x for x in range(1,11)]
print(L)
'''

'''
l=[i*2 for i in range(1,17)]
print(l)
'''

'''
l=[x for x in range(1,12) if x%2==0]
print(l)
'''

'''
l=[i+j for i in range(1,10) for j in range(1,3)]
print(l)
'''

'''
l=['abv','sda','asdasd']
k=[s.upper() for s in l]
print(k)
'''


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i,str)==True]
print(L2)

