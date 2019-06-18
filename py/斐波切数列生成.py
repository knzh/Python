
def fib(n):
    a,b=1,1
    while a<n:
        print (a,end=" ");
        a,b=b,a+b;
n=int(input('请输入斐波那契数列范围：'))
fib(n)