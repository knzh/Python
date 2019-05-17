from random import randint
num=randint(0,100)
print("Guess what I think?")

result=False #False首字母一定要大写，否则程序无法判断语句。

while result==False:
    answer=int(input())  #一定要加int（）否则程序无法判断是否是个数字。

    if answer<num:
        print("too small!")

    if answer>num:
        print("too big!")

    if answer==num:
        print("BINGO!")
        result=True
