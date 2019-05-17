def news(name):
    print("hello  "+name.title()+"!")

"""
names=["aa","ss","dd","ff"]

names=[1,2,3,4,5,6]
for names in names:
    news(str(names))
"""

i=1
name_1=[1,2,3,"a"]
name_2=[]
while name_1:
    name_3=name_1.pop()
    name_2.append(name_3)
    i+=1
    news(str(name_3))
    if i>3:
        break

