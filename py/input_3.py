word = input("你来输入一个整数，我会告诉你他是偶数还是奇数： ")
word = int(word)
if word%2==0:
    print(str(word)+"是一个整数。")
elif word%2!=0:
    print(str(word)+"是一个奇数。")