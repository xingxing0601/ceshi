# 乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(i*j, "  ", end="")
#     print("  ")

# 汉诺塔游戏规则

# def move(n, a, b, c):
#     if n == 1:
#         print(a, "->", c)
#     else:
#         move(n-1, a, c, b)
#         print(a, "->", c)
#         move(n-1, b, a, c)
#
#
#
# move(2, "A", "B", "C")
# print("*"*30)
# move(3, "A", "B", "C")

#############################################################################################

# list 列表    所有对列表的操作，原列表的地址值不改变

a = [1, 2, 3, 4, 5, 6, 7]
for x in a:
    print(x, end=",")

print()

print(a[:])

a.reverse()  # 颠倒顺序
# a.append   在列表最后位置添加值
# a.insert（m, n ）   在列表m位置前面插入值n
# a.count（m）   统计列表中的某一个值得个数
# a.copy(b)    把b列表完整的复制一份给a，结果a和b的地址不一样。
# a= [1,2,3,[10,20,30]]
#b.copy(a) 直拷贝一个地址，后面的嵌套列表地址不变，，这是浅拷贝， 而深拷贝需要特定的工具

print(a)
#-----------------------------------------------------------------------------------------------


# 元祖   元祖可以看成是不可改变的list列表  值可以是任意数据类型， 但不能修改，不能修改，不能修改。
# 总之，list所有特性，除了可修改外，元组都具有。
# 操作基本一致


t = (1,)   #括号可以加可以不加


m = 1,


a1 = [1, 2, 3, 4]

b1 = tuple(a1)   #由列表转成元祖


a2 = 1

b2 = 3

a2, b2 = b2, a2  #两个变量之间的相互转换

#-----------------------------------------------------------------------------------

#  set 集合
# 集合里面的数据是无顺序的，
# 集合里面的数据是唯一的，初始化后会自动过滤掉重复的数据。
# 添加数据   s.add(???)
# clear 只是清空数据，地址不变
# copy  拷贝
# remove    移除集合中指定的值，直接改变原有的值，如果原有的额值不存在，就会报错
# discard   移除集合中指定的值。跟remove一样，但不会报错

# pop  随机移除一个数据

# d = s.pop() 随机移除一个数据给到d







# intersection  交集


# difference  差集
# union  并集
#
# issubset 检查一个集合是否为另外一个的子集
#
# issuperset  检查一个集合是否为另外一个的超集



s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}

s_1 = s1.intersection(s2)

print(s_1)

s_2 = s1.difference(s2)

print(s_2)

s_3 = s1.issubset(s2)

print(s_3)

print(type(s1))


s5 = {1: 2, 3: 4}
print(type(s5))







