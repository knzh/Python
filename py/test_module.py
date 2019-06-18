'''
from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()
'''

'''
#可以按照如下所示的方式来区分到底要使用哪一个foo函数
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
'''
#如果将代码写成了下面的样子，那么程序中调用的是最后导入的那个foo，因为后导入的foo覆盖了之前导入的foo
'''

from module1 import foo
from module2 import foo

# 输出goodbye, world!
foo()
'''

'''
from module2 import foo
from module1 import foo

# 输出hello, world!
foo()
'''
