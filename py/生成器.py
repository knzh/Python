L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
for i in g:
    print(i)