import random
number = random.randint(1,20)
time = 0
while True:
    time +=1
    number_guess =int(input("请猜一个数"))
    if number_guess > number:
        print("数字大了")
    elif number_guess < number:
        print("数字小了")
    elif number_guess == number:
        print("你猜对了")
        break
print('你猜了%d次,正确数字是%d' %(time,number))
if time >7:
    print("你的智商欠充值")