a=1
b=0
result=False

while result==False:
    b=b+a

    if a<100:
        a=a+1

    if a==100:
        print(b)
        print(a)
        result=True





        #错误原因：执行第一个if后又继续执行了第二个if导致了b=b+a没有实现就结束了程序
