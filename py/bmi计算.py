bmi=80.5/(1.75**2)
print('小明bmi指数为','%.2f'%bmi) 
if bmi<=18.5:
    print("小明体重过轻")
elif 18<bmi<25:
    print('小明体重正常')
elif 25<=bmi<28:
    print('小明体重过重')
elif 28<=bmi<32:
    print('小明体重肥胖')
elif bmi>=32:
    print('小明体重严重肥胖')
