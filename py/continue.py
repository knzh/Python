'''
num = 0
while True:
    num +=1
    if num%2!=0:
        continue
    elif num>100:
        break
    else:
        print(num)
'''

num = 0
while True:
    num +=1
    if num%2==0:
        continue
    elif num>100:
        break
    else:
        print(num)