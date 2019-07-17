'''
def f(x):
    return (x*x)

r=map(f,[2,3,4,5,6,7,8])
print(list(r))

'''

'''
def f(x):
    return(str(x))
r=map(f,[1,2,3,4,5,6])
print(list(r))

#或者可以写成 #print(list(map(str,[1,2,3,4,5,6])))

'''

'''
from functools import reduce
def add(x,y):
    return(x*10+y)

print(reduce(add,[1,2,3,4,5,6]))
'''

'''
list={'0':2,'5':7}
print(list['5'])
'''

'''
from functools import reduce
def fn(x,y):
    return(x*10+y)

def st(x):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return(digits[x])

l=map(st,'14567223')
print(l)
m=reduce(fn,l)
print(m)
''' 

'''
from functools import reduce
# digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# (在函数外函数内此程序执行结果相同)
def str2int(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def fn(x,y):
        return x*10+y 
    def st(s):
        return digits[s] 
    return reduce(fn,map(st,s)) 
print(str2int('341561515'))
'''

'''
from functools import reduce
# digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# (在函数外函数内此程序执行结果相同)
def str2int(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
     
    def st(s):
        return digits[s] 
    return reduce(lambda x,y:x*10+y,map(st,s)) 
print(str2int('341561515'))
'''

'''
def normalize(name):
    return name[:1].upper()+name[1:].lower()
    
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''

'''
from functools import reduce
def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
'''

'''
list='1243.4324123125'
print(list.find('.'))
'''

'''
from functools import reduce
def str2float(s):
    n=s.find('.')
    s=s[:n]+s[n+1:]
    def fn(x,y):
        return x*10+y 
    def st(s):
        digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}
        return(digits[s])
    
    return reduce(fn,map(st,s))/(10**n)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
'''


