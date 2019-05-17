word = input("你来输入一个整数，我会告诉你他能否被10整除： ")
word = int(word)
if word%10==0:
    print(str(word)+"可以被10整除。")
elif word%10!=0:
    print(str(word)+"不可以被10整除。")