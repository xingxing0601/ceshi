# 上篇内容log 模块  自行查看百度

# python 语言的高级特性:
#     函数式编程(functionprogramming)
#     基于lambda演算的一种编程方式
#         程序中只有函数
#         函数可以作为参数,同样可以作为返回值
#         纯函数式编程语言:LISP, Haskell



#     python函数式编程只是借鉴函数式编程的一些特点,可以理解为一半函数一半python
#         高级函数
#         返回函数
#         匿名函数
#         装饰器
#         偏函数



# lambda表达式
#     函数:最大程度复用代码
#         存在问题:如果函数很小,很短,则会造成啰嗦.
#         如果函数调用次数少,则会造成你浪费
#         对于阅读者来说,造成阅读流程的被迫中断
#
#     lambda表达式(匿名函数)
#         一个表达式,函数体相对简单
#         不是一个代码块.仅仅是一个表达式
#         可以有参数,有多个参数也可以,用逗号隔开.
#
#     lambda表达式的用法
#     1,以lambd开头
#     2,紧跟一定的参数(可以没有)
#     3,参数后用冒号和表达式主题隔开
#     4,只是一个表达式,所以,没有return
#
# 计算一个数字的100倍数,
# 因为就是一个表达式,所以没有return
stm = lambda x: 100*x
# 使用跟函数调用一模一样
print(stm(56))


stm2 = lambda x, y, z: x+y*10+z*100
print(stm2(4, 5, 6))



# 高阶函数
#     把函数作为参数使用的函数,叫高阶函数

# 函数名就是变量,可以作为变量正常赋值,赋值后的变量就是一个函数,只是名称不一样,可以作为参数传入另一个函数。


# 系统高阶函数-map()
#     愿意就是映射,即把集合或者列表的元素,每一个元素都按照一定规则进行操作,生成一个新的列表或者集合
#     map函数就是系统提供的具有映射功能的函数,返回值是一个迭代对象

# 例子: 有一个列表里的每一个元素乘以10,并得到新的列表\
l1 = [ i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)

# 利用map函数实现

def mulTen(n):
    return n*10

l3 = map(mulTen, l1)

# map 类型是一个可迭代的结构,可以使用for循环遍历
for i in l3:
    print(i, end="")




#  reduce   归并,缩减   把一个可迭代对象给最后归并成一个结果
# 对于作为参数的函数要求: 必须有两个参数,必须有返回结果
from functools import reduce
# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x, y):
    return x + y

# 对于列表[1,2,3,4,5,6]执行myadd的reduce操作

rst = reduce(myAdd, [1, 2, 3, 4, 5, 6])

print(rst)

# filter 函数
# 过滤函数: 对一组数据进行过滤,符合条件的数据会生成一个新的列表并返回
# 跟map相比较:
#     相同:都对列表的每一个元素注意进行操作
#     不同:
#         map会生成一个跟原来数据相对应的新队列
#         filter不一定,只要符合条件的才会进入新的数据集合
# filte函数用法
#     利用给定函数进行判断
#     返回值一定是个布尔值
#     调用格式:filter(f, data), f是过滤函数, data是数据
#
# filter例子:
# 对于一个列表,对其进行过滤,偶数组成一个新列表
#
# 需要定义过滤函数
# 过滤函数要求有输入,返回布尔值

def  isEven(a):
    return a % 2 == 0

l = [1, 2, 3, 4, 5, 6, 7]

rst = filter(isEven, l)
print([i for i in rst])

# 高阶函数-排序 sorted
#     把一个序列按照给定算法进行排序.
#     key: 在排序中对每一个元素进行key函数运算,可以理解成按照key函数定义的逻辑进行排序
#     python2 和python3 相差很大
# 例子1:
a = [5, 6, 7, 1, 25, 63, 45, 89, 12]
al = sorted(a, reverse=True)
print(al)

al = sorted(a)
print(al)

# 例子2:
b = [5, 6, 7, 1, -25, 63, -45, 89, -12]
bl = sorted(b, key=abs, reverse=True)
print(bl)

# sorted()排序函数,可以对字符串列表排序




# 返回函数
#     函数可以返回具体的值
#     也可以返回一个函数作为结果

# 函数作为返回值返回,被返回的函数在函数体内定义
#例子:
def aa():
    def bb():
        print("我是bb")
        return 3
    return bb()

print(aa())






# 闭包


























