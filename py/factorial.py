def factorial(num):
    result=1
    for n in range(1,num+1):
        result *=n
    return result

n=int(input("请输入n值："))
m=int(input("请输入m值："))
print('Cn-m概率结果为：%d' %(factorial(m) // factorial(n) // factorial(m - n)))