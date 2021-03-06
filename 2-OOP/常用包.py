# -*- coding: UTF-8 -*-
# 日历
import calendar


cal = calendar.calendar(2019, l=0, c=5)
# print(cal)

# isleap : 判断某一年是否是闰年
print(calendar.isleap(2018))

# leapdays : 获取指定年份之间的闰年的个数
help(calendar.leapdays)
print(calendar.leapdays(1998, 2018))

# month() 获取某个月的日历字符串
print(calendar.month(2019, 2))

# monthrange() 获取一个月从周几开始和这个月的天数
# 格式: calendar.monthrange(年,月)
# 注意: 周默认0-6 表示周一到周天

print(calendar.monthrange(2019, 2))

w, t = calendar.monthrange(2019, 2)
print(w)
print(t)

# mothcalendar() 返回一个月的矩阵列表
# 格式:calendar.monthcalendar(年, 月)
# 返回值:耳机列表
# 注意: 矩阵中没有天数用0表示
m = calendar.monthcalendar(2019, 2)
print(m)

#  prcal : print calendar 直接打印日历
calendar.prcal(2018)


# prmonth(年,月) 打印月
calendar.prmonth(2018, 3)

# weekday() 获取周几

# 格式:calendar.weekday(年,月,日)
calendar.weekday(2018, 3, 26)


# ###########################################################################################################

# time 模块
#     时间戳
#         一个时间表示,根据不同语言,可以是整数或者浮点数
#         是从1970年1月1日0时0分0秒到现在经历的秒数
#         如果表示的时间是1970年以前或者太遥远的未来,可能出现异常
#         32位系统能够支持到2038年
#     UTC时间
#         UTC又称世界协调时间,以英国的格林泥治天文所在的地区作为参考时间,也叫世界标准时间
#         中国时间是 utc-8  东八区
#     夏令时
#         夏令时就是夏天的时候将时间调快一小时,本意是督促大家找谁早起节省蜡烛!每天变成25个小时,本质没变还是24个小时
#
#     时间元组
#         一个包含时间的普通元组
#
# 时间模块需要单独导入
import time
# 时间模块的属性
# timezone :当前时区和UTC时间相差的秒数,在没有夏令时的情况下的间隔,东八区的是-28800
# altzone  前时区和UTC时间相差的秒数,在有夏令时的情况下的间隔
# daylight 测当前是否是夏令时时间 状态,

print(time.timezone)
print(time.altzone)
print(time.daylight)


# 获取时间戳
print(time.time())
# 结果是浮点数 1546658064.5517719


# 获取当前时间
print(time.localtime())
# 结果:time.struct_time(tm_year=2019, tm_mon=1, tm_mday=4, tm_hour=17, tm_min=43, tm_sec=42, tm_wday=4, tm_yday=4, tm_isdst=0)

print(time.localtime().tm_hour)

# asctime() 返回元组的正常字符串化之后的时间格式
# 用法: time.asctime(时间元组)
# 返回值: 字符串

print(time.asctime(time.localtime()))

t = time.localtime()
tt = time.asctime(t)
print(tt)

# ctime : 获取字符串化的当前时间
print(time.ctime())

# mktime() 使用时间元组获取对应的时间戳
# 用法:time.mktime(时间元组)
# 返回值:浮点数时间戳

print(time.mktime(time.localtime()))

# clock : 获取cpu时间,3.0-3.3版本直接使用,3.6调用有问题
time.clock()
print(time.clock())

# sleep : 使程序进入睡眠状态  n秒后继续
time.sleep(1)

# strftime : 将时间元组转化成自定义的格式
'''
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
'''

# 把时间表示成,2019年1月4日 18:22
t = time.localtime(time.time())
ft = time.strftime('%Y-%m-%d %H:%M', t)
ftt = time.strftime('%Y{0}%m{1}%d{2}%H:%M').format('年', '月', '日')
print(ft)
print(ftt)

# datetime模块
#     datetime 提供日期和时间的运算和表示
#     datetime常见属性
#     datetime.date : 一个理想化的日期,提供
import datetime
print(datetime.date(2019, 1, 5))
# datetime.datetime
from datetime import datetime
# 常用类方法
#     today
#     now
#     utcnow
#     fromtimestamp: 从时间戳中返回本地时间
dt = datetime(2019, 1, 5)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta 表示一个时间间隔

from datetime import datetime, timedelta

t1 = datetime.now()
print(t1.strftime("%Y-%m-%d  %H:%M:%S"))

# td表示以小时的时间长度
td = timedelta(hours=1)

# 当前时间加上时间间隔后,把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d  %H:%M:%S"))

# timeit 时间测量工具

def p():
    time.sleep(3.6)
t2 = time.time()
p()
print(time.time() - t2 )



# ##############################################################################################################

# os 操作系统相关
#     跟操作系统相关,主要是文件操作
#     主要包含在三个模块里
#         os, 操作系统目录相关
#         os.path 系统路径相关操作
#         shutil 高级文件操作,目录树的操作,文件赋值,删除,移动.
# os 模块
#     getcwd() 获取当前的工作目录
#     格式:os.getcwd()
#     返回值:当前工作路径的字符串
#     当前工作目录就是程序都在进行文件相关操作,默认查找文件的目录
import os

print(os.getcwd())

    # chdir() 改变当前的工作目录
    # change directory
    # 格式:os.chdir('路径')
    # 返回值 : 无
# 例: os.chdir('/root/home/')


# listdir()获取一个目录中所有子目录和文件的名称列表
# 格式:os.listdir(目录路径)  默认当前目录
# 返回值:所有子目录和文件名称的列表
ld = os.listdir()
print(ld)

# makedirs()  递归创建文件夹
# 格式 : os.makedirs(递归路径)  默认当前的工作目录
# 返回值: 无
# 递归路径:多文件夹层层包含的路径就是递归路径

# rst = os.makedirs("G:/a/b/c/d")

# system() 运行系统shell命令
# 格式: os.system(系统命令)
# 返回值: 打开一个shell或者终端界面
# print(os.system("dir"))

# getenv() 获取指定的系统环境变量值
# 格式: os.getenv('环境变量名')
# 返回值: 指定环境变量名对应的值

rst = os.getenv("PATH")
print(rst)


# exit() 退出当前程序
# 格式: exit()
# 返回值 :无


# 值部分(在写代码的时候尽量不要手动拼写地址,因为手动拼写的路径可能不具有移植性)
# 例:
#     print("/home/tlxy" + "/" + "/a/b")
#     os.curdir : currentn dir ,当前目录
#     os.pardir :  parent dir , 父目录
#     os.sep :当前系统的路径分隔符
#     os.linesep: 当前系统的换行符
#           windows : "\r\n"
#           unix,linux,macos :"\n"
#     os.name : 当前系统名称
print("*"*30)
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)
print(os.name)



print("*" * 30)
# os.path模块 ,跟路径相关的模块
# abspath()将路径转化成绝对路径
# 格式:os.path.abspath('路径')
# 返回值:路径的绝对路径形式

absp = os.path.abspath('.')
print(absp)


# basename() 获取路径中的目录名最后一部分
# 格式:os.path.basename(路径)
# 返回值:文件名字符串
# bn = os.path.basename("/a/b/c/d")  打印结果为"d"

# join() 将多个路径拼合成一个路径
# 格式: os.path.join(路径1, 路径2....)
# 返回值:组合之后的新路径字符串

bd = "\home\\tlxy"
fn = "dana.haha"
p = os.path.join(bd, fn)
print(p)

# split() 将路径切割为文件夹部分和当前文件部分
# 格式:os.path.split(路径)
# 返回值 : 路径和文件名车组成的元组
t = os.path.split("\home\tlxy\dana.haha")
print(t)
# 或者
d, p = os.path.split("\home\\tlxy\dana.haha")
print(d, p)

# isdir() 检测是否是目录
# 格式: os.path.isdir(路径)
# 返回值:布尔值



# exists() 检测文件或者目录是否存在
# 格式:os.path.exists(路径)
# 返回值:布尔值

# ##############################################################################


# shutil 模块


# copy() 复制文件
# 格式 : shutil.copy(来源路径,目标路径)
# 返回值: 返回目标路径
# 拷贝的同时,可以给文件重命名
import shutil
# print(shutil.copy("来源路径", "目标路径"))


# copy2() 复制文件,保留原数据(文件信息)
# 格式: shutil.copy2("来源路径","目标路径")
# 返回值:返回目标路径
# 注意: copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据



# copyfile() 将一个文件的内容复制到另一个文件当中
# 格式: shutil.copyfile("源路径", "目标路径")
# 返回值 :无
# print(shutil.copyfile("源目标", "目标路径"))


# move() 移动文件/文件夹
# 格式:shutil.move("原路径", "目标路径")
# 返回值:无


# ########################################################################################

# 归档和压缩
#     归档:把多个文件或者文件夹合并到一个文件当中
#     压缩:用算法把多个文件或者文件夹无损或者有损合并到一个文件当中

# make_archive() 归档操作
# 格式 : shutil.make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')
# 返回值:归档之后的地址

# unpack_archive() 解包操作
# 格式:shutil.unpack_archive('归档文件地址','解包之后的地址')
# 返回值:解包之后的地址



# zip 压缩包  模块: zipfile
import zipfile
# zf = zipfile.ZipFile("zip文件名") # 创建一个zipfile对象,表示一个zip文件.参数表示文件的路径或者类文件对象
# rst = zf.getinfo("name") # 获取zip文档内指定文件的信息,返回一个zipfile.Zipfile对象,它包括文件的详细信息
#
# zipfile(名称例如:zf).namelist()  #获取zip文档中所有文件的名称列表 ,无参数
# zipfile(名称例如:zf).extractall("参数") # 解压zip文档中的所有文件到当前目录.参数为zip文档的所有文件名称列表
# 例: rst = zf.extractall("解压到那个目录路径")


# ############################################################################

# random 随机数
# 所有的随机模块都是伪随机

# random（） 获取0-1之间的随机小数
# 格式： random.random()
# 返回值:随机0-1之间的小数
import random
print(random.random())
print(random.randint(0, 101))  # 随机获取指定单位内的整数


# choice() 随机返回序列中的某个值
# 格式: random.choice(序列)
# 返回值: 序列中的某个值
l = [str(i)+ "haha" for i in range(10)]
print(l)

rst = random.choice(l)
print(rst)


# shuffle() 随机打乱列表
# 格式:random.shuffle(列表)
# 返回值:打乱顺序之后的列表
l1 = [i for i in range(10)]
random.shuffle(l1)
print(l1)


# randint(a, b) : 返回一个a到b之间的随机整数,包含a和b
print(random.randint(100, 200))



