# def is_old(n):
    # return n % 2 == 0
# print(list(filter(is_old,[1,2,3,4,5,6,7,8,9,])))

# python的and 返回值
# >>> 'a' and 'b'
# 'b'
# >>> '' and 'b'
# ''
# >>> 'b' and ''
# ''
# >>> 'a' and 'b' and 'c'
# 'c'
# >>> '' and None and 'c'
# ''
# 在布尔上下文中从左到右演算表达式的值，如果布尔上下文中的所有值都为真，那么 and 返回最后一个值。

# def no_empty(s):
    # return s and s.strip()
# print(list(filter(no_empty,['x','z','a','',None,'jhgjf',])))

# def _odd_iter():
    # n = 1
    # while True:
        # n=n+2
        # yield n

# def _not_divisible(n):
    # lambda x:x % n > 0

# def primes():
    # yield 2
    # it = _odd_iter()
    # while True:
        # n = next(it)
        # yield n
        # it = filter(_not_divisible(n),it)
# for n in primes():
    # if n<1000:
        # print(n)
    # else:
        # break

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return str(n)==str(n)[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')



