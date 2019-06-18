for i in range(2,1000):
    i_b=int(i/100)
    i_s=int(i%100/10)
    i_g=int(i%10)
#print('这个数百位是%d，十位是%d，个位是%d' %(i_b,i_s,i_g))
    if i_b**3+i_s**3+i_g**3 ==i:
        print("%d是水仙花数" %i)