# coding=gbk

'''
第二章 基础内容
'''
r
import datetime

dt = datetime.datetime(2011, 10, 29, 20, 20, 10)

print(dt)
# 2011-10-29 20:20:10

print(dt.minute)
# 20

print(dt.date())
# 2011-10-29

print(dt.time())
# 20:20:10

print(dt.strftime('%m/%d/%Y %H:%M')) #strftime方法可以将datetime转换成字符串 # 10/29/2011 20:20
# print(type(dt.strftime('%m/%d/%Y %H:%M')))
# <class 'str'>

print(datetime.datetime.strptime('20090108','%Y%m%d')) #strptime函数可以将字符串转换成日期对象
# 2009-01-08 00:00:00
# print(type(datetime.datetime.strptime('20090108','%Y%m%d')))
# <class 'datetime.datetime'>

print(datetime.datetime.strptime('2022-12-13 -0800', '%Y-%m-%d %z')) # %z 格式为 +HHMM或-HHMM的UTC时区偏移；如果没有时区则为空
# 2022-12-13 00:00:00-08:00

dt2 = datetime.datetime(2008, 1, 1, 18, 30, 55)
print(dt-dt2) #两个不同的datetime对象会产生一个datetime.timedelta类型的对象
# 1397 days, 1:49:15
# print(type(dt-dt2))
# <class 'datetime.timedelta'>

print(dt2+datetime.timedelta(1,10)) #此处的1和10代表1天又10秒，将timedelta加到一个datetime上将产生一个新的对象
# 2008-01-02 18:31:05


# range产生的整数包含起始但不包含结尾，所以可用来根据序列的索引遍历序列
# 起始、结尾、步进(可以是负值)都可以传递给range函数
print(list(range(10)))
print(list(range(10,-10,-2)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]


# 三元表达式允许你将一个if-else代码块整合在一行代码或语句中生成数据；以下两个表达式的效果是一样的
x = 5
if x > 0:
    print('x是正数')
else:
    print('x是非正数')

# 等价于
print('x是正数') if x > 0 else print('x是非正数') # 如果条件很复杂，可读性会比较差

# coding=gbk

# 第三章 内建数据结构、函数及文件

'''
内建功能
'''

# 元组
# 创建元组的最简便方法就是用逗号分隔序列值
tup = 1,10,100
print(tup) # (1, 10, 100)

# 可以生成 元素是元组的元组，如：((1, 2, 3), (123, 321))
print(tuple([(1,2,3),(123,321)]))

#tuple函数可以将列表或迭代器转换成元组
print(tuple([1,2,3]))
print(tuple('hello'))
# (1, 2, 3)
# ('h', 'e', 'l', 'l', 'o')

# 尽管元组一旦创建后其各个位置上的对象就无法被修改了，但如果元组中的一个对象是可变的，例如列表，你可以在其内部进行修改
tup = tuple(('hello','world',[1,0,3]))
print(tup) # ('hello', 'world', [1, 0, 3])
tup[2].append(100) # append方法只能吸纳一个变量
print(tup) # ('hello', 'world', [1, 0, 3, 100])

# 可以用+号来连接生成更长的元组
print((1,0,10)+('hello','world')) # (1, 0, 10, 'hello', 'world')

# 可以用*号来拷贝元组
print(('hello','world')*3) # ('hello', 'world', 'hello', 'world', 'hello', 'world')

# 元组拆包
seq = [(1,2,3), (4,5,6), (7,8,9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))
    '''
    a=1, b=2, c=3
    a=4, b=5, c=6
    a=7, b=8, c=9'''

# *rest是一种特殊语法，用于在函数调用时获取任意长度的位置参数列表； 这部分有时是你想丢弃的数据，实操中可以用“*_”来表示
values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a, b, rest) # 1 2 [3, 4, 5]


#列表
# append方法可以将元素添加到列表的尾部
# insert方法可以将元素插入到指定的列表位置
b_list = ['red','green', 'yellow']
b_list.insert(1,'blue')
print(b_list) # ['red', 'blue', 'green', 'yellow']

# pop方法可以将特定位置的元素移除并返回；如果此处不填位置参数，则默认是最后一个元素
b_list = ['red','green', 'yellow']
print(b_list.pop(1)) # green [如果此处不填位置参数，则默认是最后一个元素]
print(b_list) # ['red', 'yellow']

# remove方法可以定位第一个符合要求的值并移除他
c_list = ['happy', 'sad', 'excited', 'nervous', 'sad']
c_list.remove('sad')
print(c_list) # ['happy', 'excited', 'nervous', 'sad']

# (not) in 关键字可以检查某个值是否在列表中
print('happy' not in c_list) # False

# extend方法可以向目标列表添加多个元素，虽然“+”也可以，但是运行效率较低；
list_1 = ['one', 'two']
list_1.extend(['three','four']) # ['one', 'two', 'three', 'four']
list_1.append(['three','four']) # ['one', 'two', 'three', 'four', ['three', 'four']]

# bisect.bisect会找到元素应当被插入的位置，并保持序列排序；使用它以前一定要保证列表已经提前排好序
import bisect
c = [1, 2, 3, 3, 7, 9, 12]
print(bisect.bisect(c, 5)) # 4
# bisect.insort可以将元素插入到相应位置
bisect.insort(c, 5.9)
print(c) # [1, 2, 3, 3, 5.9, 7, 9, 12]

# 切片
seq = [7, 3, 2, 5, 6, 7, 9, 12, 22, 2, 99]
print(seq[3:6]) # [5, 6, 7]
seq[1:3] = [99, 100]
print(seq) # [7, 99, 100, 5, 6, 7, 9, 12, 22, 2, 99]
print(seq[2:6:2]) # [100, 6]
print(seq[-6::2]) # [7, 12, 2]
print(seq[-6::-1]) # [7, 6, 5, 100, 99, 7]

#序列函数
# enumerate函数 可以返回(i, value)元组的序列，其中value是元素的值，i是元素的索引
adhoc_list = ['shenzhen', 'shanghai', 'beijing']
mapping_result = {}
for i, v in enumerate(adhoc_list):
    mapping_result[v] = i

print(mapping_result) # {'shenzhen': 0, 'shanghai': 1, 'beijing': 2}

# sorted函数 可以返回一个根据任意序列中的元素新建的已排序列表
print(sorted([4, 5, 9, 33, 1, 3, 100, 4, 22, 2])) #[1, 2, 3, 4, 4, 5, 9, 22, 33, 100]
# ,reverse=True

# zip函数 可以将列表、元组、或其他序列的元素配对，新建一个元组构成的列表；输出前记得要套上一层list
seq1 = ['china', 'japan', 'australia']
seq2 = ['shanghai', 'yokohama', ['melbourne','sydney']]
zipped_result = zip(seq1, seq2)
print(list(zipped_result)) # [('china', 'shanghai'), ('japan', 'yokohama'), ('australia', ['melbourne', 'sydney'])]
# zip生成的列表长度由最短的序列决定
seq3 = [True, False]
print(list(zip(seq1, seq2, seq3))) # [('china', 'shanghai', True), ('japan', 'yokohama', False)]

# zip搭配enumerate 遍历多个序列
for i, (a, b, c) in enumerate(list(zip(seq1, seq2, seq3))):
    print("{0}: {1};{2};{3}".format(i, a, b, c))
    # 0: china;shanghai;True
    # 1: japan;yokohama;False


# 字典
dt = {'china':['shanghai', 'beijing'], 'japan':['tokyo'], 'korea':['soul']}
print('korea' in dt) # 用来检查字典中是否含有该键key (值value不行)

# del关键字 以及 pop方法 都可以删除值
del dt['japan']
print(dt) # {'china': ['shanghai', 'beijing'], 'korea': ['soul']}
popvalue = dt.pop('korea')
print(popvalue) # ['soul']
print(dt) # {'china': ['shanghai', 'beijing']}

dt['german'] = 'berlin' # {'china': ['shanghai', 'beijing'], 'german': 'berlin'}
dt.update({'german':'hamburg', 'canada':['toronto','vancouver']}) # {'china': ['shanghai', 'beijing'], 'german': 'hamburg', 'canada': ['toronto', 'vancouver']}

key_list = ['monday', 'tuesday', 'saturday', 'sunday']
value_list = ['basketball', ['study', 'rope'], ['basketball', '8-ball'], 'football']
dt2 = {}
for i, k in zip(key_list, value_list):
    dt2[i] = k

print(dt2)
# {'monday': 'basketball', 'tuesday': ['study', 'rope'], ' saturday': ['basketball', '8-ball'], 'sunday': 'football'}

print(dt2.get('saturday')) # ['basketball', '8-ball']
print(dt2.get('wednesday','not found')) # not found

dt3 = ['apple','orange', 'banana', 'peach', 'pear']
fruit_dic = {}
for i in dt3:
    firstword = i[0]
    fruit_dic.setdefault(firstword, ['not in']).append(i)

print(fruit_dic) # {'a': ['not in', 'apple'], 'o': ['not in', 'orange'], 'b': ['not in', 'banana'], 'p': ['not in', 'peach', 'pear']}

# 集合
# 集合是一种无序且元素唯一的容器，他类似字典但没有键只有值，不可以是列表，可以是元组 （总之，元素不可变）
print(set([1, 2, 2, 5, 5, 99, 100, 22, 23, 33, 199])) # {1, 2, 99, 100, 5, 33, 199, 22, 23}
print({1, 2, 2, 5, 5, 99, 100, 'happy', 23, 33, 199, 'happy', 'world'}) # {1, 2, 99, 100, 5, 33, 199, 'world', 'happy', 23}

# 集合可以支持数学上的集合操作

# 对于大型集合，下面的写法效率更高
a = {1, 2, 3, (4, 99), 5}
b = {3, 4, 5, 6, 7, 8}
c = a.copy()
c |= b # 将c的内容设置为c和b的并集；也可以写成 c.update(b)
print(c) # {1, 2, 3, 4, 5, 6, 7, (4, 99), 8}


# 列表推导式 expr for val in collection if condition
strings = ['a', 'an', 'bee', 'sea', 'will', 'tiger', 'working_day']
print([len(i) for i in strings if True]) # [1, 2, 3, 3, 4, 5, 11]

# 集合推导式 还可以搭配map函数 map(function, iterables):the function to execute for each item
print(set(map(len,strings))) # {1, 2, 3, 4, 5, 11}

# 字典推导式
loc_mapping = {k:vv for vv,k in enumerate(strings)}
print(loc_mapping)

# 找出所有包含两个以上字母e的名字
all_data = [['cheer', 'john', 'smith', 'steven', 'jack'], ['alice', 'ben', 'thomas', 'max', 'bob', 'lee']]
name_list = []
for names in all_data:
    enough_e = [name for name in names if name.count('e') > 1]
    name_list.extend(enough_e)

print(name_list) # ['cheer', 'steven', 'lee']

# 嵌套列表推导式
name_list2 = [name for names in all_data for name in names if name.count('e') > 1]
print(name_list2) # ['cheer', 'steven', 'lee']


'''
函数
'''
def my_fuc(x, y):
    if x > y:
        return 'x is bigger than y'
    elif x < y:
        return 'y is bigger than x'
    else:
        return 'they are the same figure'

print(my_fuc(100, 88)) # x is bigger than y

# 参数x会在函数退出时被销毁
# print(x) # NameError: name 'x' is not defined
# 在函数外部给变量赋值是可以的，但这些变量必须使用global关键字声明为全局变量
def my_func2(xx):
    global yy
    yy = xx * 2
    print('l have outputted ' + xx + 'twice')

my_func2('happy day!') # l have inputted happy day!
print(yy) # happy day!happy day!

# 指定列表中第二个元素来进行排序
tuple_list = [(3,5), (2,11), (7,9), (21,2)]
def second_element(parse):
    return parse[1]

tuple_list.sort(key=second_element)
print(tuple_list) # [(21, 2), (3, 5), (7, 9), (2, 11)]

# Lambda函数，可以通过单个语句生成函数；其结果是返回值
strings = ['aaa', 'abbasb', 'abccc', 'abcd']
strings.sort(key=lambda x: len(set(list(x)))) # 根据字符串中不同字母的数量对字符串进行排序
print(strings) # ['aaa', 'abbasb', 'abccc', 'abcd']


def fucc(alist, f):
    return [f(x) for x in alist]

print(fucc([2,3,5,10], lambda y: round(y**(1/2),2))) # [1.41, 1.73, 2.24, 3.16]

# 生成器 部分 [e.g. itertools模块] 待研究。。。

# 错误和异常处理
# 可以通过将多个异常类型写成元组的方式同时捕获多个异常
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x
    finally:
        print('这段文字无论try代码块是否报错都要执行')


'''
文件与操作系统
此章重在理解python如何处理文件的基础知识
'''

# 使用with语句，文件会在with代码块结束后自动关闭
with open(r'C:\Users\Ben\Desktop\pythonfile.txt') as ff:
    content = [x.rstrip() for x in ff] #或者ff.readlines()也可以
print(content) # ['today is a good day', 'l had the l with my best friend - twd in Hongkou District', 'l went there by bike, and rode back as well', 'feel full and happy']


# 如果我们写下 f=open(path, 'w'),一个新的文件会在path的位置被创建，并在同一路径下覆盖同名文件；
# 还有一种'x'文件模式，他会创建可写的文件，但如果给定path下已经存在同名文件的话就会创建失败

# with open(r'C:\Users\Ben\Desktop\pythonfile2.txt','x')as ff2:
#     ff2.write('new hello world!')
#     ff2.write('\n换行：hello world!')

# 默认情况下，文件是以只读模式'r'打开的；
# 模式'r+'是读写模式

# 模式'a' 是添加到已经存在的文件（如果不存在，就创建一个）

# 复制一个当前已有的文件，且确保内容中没有空行 (自己写的方法)
with open(r'C:\Users\Ben\Desktop\pythonfile.txt') as original:
    content = [i for i in original.readlines() if len(i)>1]

print(content)

with open(r'C:\Users\Ben\Desktop\pythonfile_copy.txt', mode='w') as new:
    new.writelines(content)

# 复制一个当前已有的文件，且确保内容中没有空行 (书上的方法)
with open(r'C:\Users\Ben\Desktop\pythonfile_copy2.txt',mode='w') as new2:
    new2.writelines(j for j in open(r'C:\Users\Ben\Desktop\pythonfile.txt') if len(j) > 1) # 存疑：目标源文件是否被自动关闭

with open(r'C:\Users\Ben\Desktop\pythonfile_copy2.txt') as ff:
    tt = ff.readlines()

print(tt)

# seek(position)方法：移动到指定的位置()
# tell() 返回当前的文件位置，返回值是整数

# coding=gbk

# 第四章 NumPy基础
import numpy as np

# N维数组对象(ndarray)，允许你使用类似于标量的操作语法在整块数据上进行数学计算
data = np.random.randn(2,3) # 生成一个2行3列的随机数组
print(data)
print(data * 10)

# 一个ndarray所包含的每一个元素均为相同类型；每一个数组都有一个shape属性用来表示每一维度的数量；也都有一个dtype属性用来描述数组的数据类型
print(data.shape) # (2, 3)
print(data.dtype) # float64

# 生成数组的方式1
arr1 = np.array([1,2,3,4,5])
print(arr1) # [1 2 3 4 5]

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12.5,13,14,15]]) # 如果嵌套序列，那么将会自动转换成多维数组
print(arr2)
# [[ 1.   2.   3.   4.   5. ]
#  [ 6.   7.   8.   9.  10. ]
#  [11.  12.5 13.  14.  15. ]]
print(arr2.ndim) # 2
print(arr2.dtype) # float64
print(arr2.shape) # (3, 5)
print(np.array([[[1,2,3],[2,3,4]],[[1,2,3],[2,3,4]],[[1,2,3],[2,3,4]]]).ndim) # 3

# 生成数组的方式2
print(np.ones((2,4,3),str)) # zeros可以一次性创建全0的数组，ones可以一次性创建全1数组
# [[['1' '1' '1']
#   ['1' '1' '1']
#   ['1' '1' '1']
#   ['1' '1' '1']]
#
#  [['1' '1' '1']
#   ['1' '1' '1']
#   ['1' '1' '1']
#   ['1' '1' '1']]]

# 生成数组的方式3
# arange是python内建函数range的数组版
print(np.arange(8)) # [0 1 2 3 4 5 6 7]

# 可以使用astype方法来转换数组的数据类型
print(np.array([1,2,3],dtype=str).astype(float)) # [1. 2. 3.]

# 数组算术
# 所有在两个等尺寸数组之间的算数操作都应用了逐元素操作的方法
arr = np.array([[1,2,3],[10,11,12]])
print(arr * arr)
# [[  1   4   9]
# [100 121 144]]
print(arr == (arr*arr))
# [[ True False False]
#  [False False False]]

# 数组的索引与切片
# 一维数组与列表较为类似
arr = np.arange(5)
print(arr[2:4]) # [2 3]
arr_slice = arr[1:3]
arr_slice[:] = 99
print(arr) # [ 0 99 99  3  4]
arr_slice[1] = 98 # 数组的切片是原数组的视图，这意味着数据并不是被复制了，任何对于视图的修改都将反映到原数组上
print(arr)
# 如果你想要一份数组切片的拷贝而不是一份视图，可以使用类似 arr[5:8].copy()

# 在多维数组中，索引返回的对象僵尸降低一个维度的数组；比如在一个二维数组中，每一个索引值对应的元素不再是一个值，而是一个一维数组；单个元素可以通过递归的方式或者索引含逗号的方式来获得。
arr = np.array([[1,2,3],[7,8,9],[11,22,33]])
print(arr[1]) # [7 8 9]
print(arr[1][2]) # 9
print(arr[1,2]) # 9

print(arr[:2]) #切片索引前两行
# [[1 2 3]
#  [7 8 9]]
print(arr[:2,1:])
# [[2 3]
#  [8 9]]

# 单独一个冒号表示选择整个轴上的数组
# 对切片表达式赋值时，整个切片都会重新赋值

# 布尔索引
name_list = np.array(['Bob', 'Tom', 'Bob', 'Steven', 'Sam'])
data = np.random.randn(5,4) # 假设让上面五个人每个人都被分配一行四列的数字
print(name_list == 'Bob') # [ True False  True False False]
print(data[name_list == 'Bob']) # 找到所有Bob对应的数据
print(data[name_list != 'Bob']) # 找到除Bob以外其他人对应的数据
print(data[~(name_list == 'Bob')]) # 找到除Bob以外其他人对应的数据
print(data[(name_list == 'Bob')|(name_list == 'Sam')]) # 找到所有Bob和Sam对应的数据
# python的关键字and，or对布尔值数组是没有效果的，请使用 &，|

data[name_list == 'Bob'] = 99 # 利用一维布尔值数组对每一行设置数值
print(data)
data[data < 0] *= -1 # 把所有负值都设置为相反数
print(data)

# 神奇索引(使用整数数组进行数据索引) -- 待研究

# 数组转置和换轴
arr = np.arange(15).reshape((3,5))
print(arr)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
print(arr.T)
# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]

# transpose方法,参数是0，1，2，
# 第0个维度：对应有多少个二维数组
# 第1个维度：对应每个二维数组的行数
# 第2个维度：对应每个二维数组的列数


# 将条件逻辑作为数组操作
arr1 = np.array([1,2,3])
arr2 = np.array([5,9,10])
logic = np.array([True,False,True])
result = np.where(logic, arr1, arr2) # np.where的第二个和第三个参数并不需要是数组，他们可以是标量
print(result) # [1 9 3]

# 数组统计函数
arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[11,22,33,44,55,66]])
print(arr.mean(axis=1)) # [ 3.5  9.5 38.5]
print(arr.mean(axis=0)) # [ 6.33333333 10.66666667 15.         19.33333333 23.66666667 28.        ]
print(arr.cumsum(axis=1))
# [[  1   3   6  10  15  21]
#  [  7  15  24  34  45  57]
#  [ 11  33  66 110 165 231]]
print(arr.cumprod(axis=0))
# [[   1    2    3    4    5    6]
#  [   7   16   27   40   55   72]
#  [  77  352  891 1760 3025 4752]]

# 布尔值数组
arr = np.array([[True, False, True, False, True]])
print((arr>0).sum()) # 3
print(arr.any()) # True
print(arr.all()) # False

# 线性代数
arrx = np.array([[1,2,3],[4,5,6]])
arry = np.array([[-1,1],[4,-5],[2,2]])
print(arrx.dot(arry)) # 等价于 np.dot(arrx, arry) 和 arrx @ arry [特殊符号@可以作为中缀操作符，用于点乘矩阵操作]
# [[13 -3]
#  [28 -9]]

# coding=gbk

# 第五章 Pandas入门
import pandas as pd

'''
pandas数据结构介绍
'''

# series 一维的数组型对象
obj = pd.Series(['one','two','three'])
# 0      one
# 1      two
# 2    three

# 默认生成的索引是0到N-1,N是数据长度
print(obj.values) # ['one' 'two' 'three']

# 可以用标签来标识每一个数据点
obj2 = pd.Series([80, 99, 87, 75], index=['Park', 'James', 'Kobe', 'Durant'])
print(obj2)
# Park      80
# James     99
# Kobe      87
# Durant    75
print(obj2['Kobe']) # 87
print(obj2[obj2>90]) # James    99
print(obj2[obj2>90] * 2) # James    198

# Series可以被认为是一个长度固定且有序的字典，因为他将索引值和数据值按位置配对
print('Iverson' in obj2) # False
print('James' in obj2) # True

# 可以用字典生成一个Series
obj3 = {'Chelsea':95, 'Manchester City':97, 'Liverpool':[95,96], 'Hotspur':94}
print(pd.Series(obj3))
# Chelsea                  95
# Manchester City          97
# Liverpool          [95, 96]
# Hotspur                  94

obj4 = pd.Series([80, 99, 87, 75, None], index=['Tony', 'Ben', 'Steven', 'Bonnie', 'Amber'])
print(pd.isnull(obj4))
# Tony      False
# Ben       False
# Steven    False
# Bonnie    False
# Amber      True

# 由于Series可以自动对齐索引，所以可以进行数学操作，可以靠join来理解


# DataFrame表示的是矩阵的数据表，既有行索引也有列索引

data = {
    'Team': ['Manchester City', 'Liverpool', 'Chelsea', 'Manchester United', 'Asenal'],
    'Player': ['Akun', 'Lampard', 'Mane', 'Ronald', 'Henry'],
    'Goal': [30, 28, 25, 24, 20]
}

dashboard = pd.DataFrame(data=data, columns=['Team', 'Player', 'Goal', 'Score'])
print(dashboard)
#                 Team   Player  Goal Score
# 0    Manchester City     Akun    30   NaN
# 1          Liverpool  Lampard    28   NaN
# 2            Chelsea     Mane    25   NaN
# 3  Manchester United   Ronald    24   NaN
# 4             Asenal    Henry    20   NaN

# 对于大型的Dataframe，head方法将会只选出头部的五行

print(dashboard[['Team','Score']].loc[1,'Team']) # Liverpool

dashboard['Score'] = 99
print(dashboard)
#                 Team   Player  Goal  Score
# 0    Manchester City     Akun    30     99
# 1          Liverpool  Lampard    28     99
# 2            Chelsea     Mane    25     99
# 3  Manchester United   Ronald    24     99
# 4             Asenal    Henry    20     99

# 当你用列表或者数组给一个列赋值时，值的长度必须和DataFrame的长度相匹配； 但你如果是用Series赋值给一列，Series的索引将会按照DataFrame的索引重新排列，并在空缺的地方填充缺失值
fill_speed = pd.Series([98,99,95], index=[0, 2, 3])
dashboard['Speed'] = fill_speed
print(dashboard)
#                 Team   Player  Goal  Score  Speed
# 0    Manchester City     Akun    30     99   98.0
# 1          Liverpool  Lampard    28     99    NaN
# 2            Chelsea     Mane    25     99   99.0
# 3  Manchester United   Ronald    24     99   95.0
# 4             Asenal    Henry    20     99    NaN

top1player = dashboard[(dashboard['Goal'] > 25) & (dashboard['Speed'] > 95)]
print(top1player)
#               Team Player  Goal  Score  Speed
# 0  Manchester City   Akun    30     99   98.0

del dashboard['Score']
print(dashboard.columns.values) # ['Team' 'Player' 'Goal' 'Speed']
print(dashboard.values) # DataFrame的values属性会将包含在DataFrame中的数据以二维ndarray的形式返回
# [['Manchester City' 'Akun' 30 98.0]
#  ['Liverpool' 'Lampard' 28 nan]
#  ['Chelsea' 'Mane' 25 99.0]
#  ['Manchester United' 'Ronald' 24 95.0]
#  ['Asenal' 'Henry' 20 nan]]

# 如果嵌套字典被赋值给DataFrame, pandas会将字典的键作为列，将内部字典的键作为行索引
goaldata = {'Ronald': {2013: 30, 2014: 31, 2015: 35}, 'Messi': {2013: 31, 2014: 31, 2015: 32, 2016: 33}}
print(pd.DataFrame(goaldata))
#       Ronald  Messi
# 2013    30.0     31
# 2014    31.0     31
# 2015    34.0     32
# 2016     NaN     33

# 对DataFrame进行转置操作
print(pd.DataFrame(goaldata).T)
#         2013  2014  2015  2016
# Ronald  30.0  31.0  34.0   NaN
# Messi   31.0  31.0  32.0  33.0


'''
Series或DataFrame中数据交互的基础机制
'''

#reindex方法可以创建一个符合新索引的新对象
rankboard = pd.DataFrame(
    {'PlayerName':['Lebron','Harden','Durant','Curry'],
     'Score':[32,31,29,28.5]}
)
#   PlayerName  Score
# 0     Lebron   32.0
# 1     Harden   31.0
# 2     Durant   29.0
# 3      Curry   28.5

print(rankboard.reindex(['top1',1,2,'3']))
#      PlayerName  Score
# top1        NaN    NaN
# 1        Harden   31.0
# 2        Durant   29.0
# 3           NaN    NaN

# method可选参数可以允许我们在重建索引时插值，ffill为前向填充，bfill是后向填充
print(rankboard.reindex(range(5),method='ffill'))
#   PlayerName  Score
# 0     Lebron   32.0
# 1     Harden   31.0
# 2     Durant   29.0
# 3      Curry   28.5
# 4      Curry   28.5
print(rankboard.reindex([-1,0,1,2,3,4],method='bfill'))
#    PlayerName  Score
# -1     Lebron   32.0
#  0     Lebron   32.0
#  1     Harden   31.0
#  2     Durant   29.0
#  3      Curry   28.5
#  4        NaN    NaN

# 列可以使用columns关键字重建索引
col = ['PlayerName','Age','Score']
print(rankboard.reindex(columns=col))
#   PlayerName  Age  Score
# 0     Lebron  NaN   32.0
# 1     Harden  NaN   31.0
# 2     Durant  NaN   29.0
# 3      Curry  NaN   28.5

# 使用loc进行更高效的标签索引
print(rankboard.loc[[0,2],['PlayerName']])
#   PlayerName
# 0     Lebron
# 2     Durant

# fill_value可以通过重新索引引入缺失数据时引用的替代值
print(rankboard.reindex([0,1,2,4],columns=['PlayerName','Score','Age'],fill_value='Unknown'))
#   PlayerName    Score      Age
# 0     Lebron     32.0  Unknown
# 1     Harden     31.0  Unknown
# 2     Durant     29.0  Unknown
# 4    Unknown  Unknown  Unknown

# 在调用drop时使用标签序列会根据行标签删除值，返回的是一个新对象
print(rankboard.drop([1]))
#   PlayerName  Score
# 0     Lebron   32.0
# 2     Durant   29.0
# 3      Curry   28.5

# 可以通过传递axis='columns'或axis=1来从列中删除值
print(rankboard.drop(['Score'],axis='columns'))
#   PlayerName
# 0     Lebron
# 1     Harden
# 2     Durant
# 3      Curry

# 索引，选择，过滤
businessdashboard = pd.DataFrame(
    {
        'CompanyName':['Microsoft','Google','Amazon','Tencent','Alibaba','IBM','Intel'],
        'PerformanceIndex':[95,98,97,92,90,92,89],
        'FamousIndex':[99,99,98,90,92,94,97],
        'ScaleIndex':[96,99,95,95,96,93,94],
        'CN_Entity':[False,False,False,True,True,False,False]
    }
)
print(businessdashboard[['CompanyName','CN_Entity']])
#   CompanyName  CN_Entity
# 0   Microsoft      False
# 1      Google      False
# 2      Amazon      False
# 3     Tencent       True
# 4     Alibaba       True
# 5         IBM      False
# 6       Intel      False

print(businessdashboard[2:4][['CompanyName','ScaleIndex']])
#   CompanyName  ScaleIndex
# 2      Amazon          95
# 3     Tencent          95

print(businessdashboard[(businessdashboard['CN_Entity'] == True)&(businessdashboard['ScaleIndex']>95)])
#   CompanyName  PerformanceIndex  FamousIndex  ScaleIndex  CN_Entity
# 4     Alibaba                90           92          96       True

# 使用loc和iloc选择数据
# 轴标签loc，整数标签iloc
print(businessdashboard.loc[[1,2,4],['CompanyName','FamousIndex']])
#   CompanyName  FamousIndex
# 1      Google           99
# 2      Amazon           98
# 4     Alibaba           92

print(businessdashboard.iloc[[2,4],[1,2,3]])
#    PerformanceIndex  FamousIndex  ScaleIndex
# 2                97           98          95
# 4                90           92          96

# 索引功能也可以带上切片
print(businessdashboard.loc[:2,'CompanyName':'ScaleIndex'])
#   CompanyName  PerformanceIndex  FamousIndex  ScaleIndex
# 0   Microsoft                95           99          96
# 1      Google                98           99          99
# 2      Amazon                97           98          95

print(businessdashboard.iloc[:2,:4][businessdashboard.ScaleIndex>96])
#   CompanyName  PerformanceIndex  FamousIndex  ScaleIndex
# 1      Google                98           99          99

#df.at[];df.iat[] 可以根据行列标签/整数位置 选择单个标量值
print(businessdashboard.loc[[2],['CompanyName']])
#   CompanyName
# 2      Amazon
print(businessdashboard.at[2,'CompanyName']) # Amazon

# get_value方法，set_value方法 可以根据行列标签来设置单个值
print(businessdashboard._get_value(2,'CompanyName')) # Amazon
print(businessdashboard._set_value(2,'CompanyName','Airwallex'))
print(businessdashboard)
#   CompanyName  PerformanceIndex  FamousIndex  ScaleIndex  CN_Entity
# 0   Microsoft                95           99          96      False
# 1      Google                98           99          99      False
# 2   Airwallex                97           98          95      False
# 3     Tencent                92           90          95       True
# 4     Alibaba                90           92          96       True
# 5         IBM                92           94          93      False
# 6       Intel                89           97          94      False

df1 = pd.DataFrame(
    {'Chinese':[123,123,110,115,120,132],
     'Math':[139,123,130,128,140,132],
     'English':[134,123,122,125,150,122]
     },
    index=['Alice','Bob','Chloe','Danny','Elaine','Fannie']
)
df2 = pd.DataFrame(
    {'Chinese':[124,123,130,113,123,131],
     'Math':[139,123,132,124,132,132],
     'English':[114,129,122,121,120,112]
     },
    index=['Alice','Bill','Carrie','Derek','Eva','Fred']
)
print(df1+df2) # 行列标签完全一样，且没有NaN，才会被正常相加
#         Chinese   Math  English
# Alice     247.0  278.0    248.0
# Bill        NaN    NaN      NaN
# Bob         NaN    NaN      NaN
# Carrie      NaN    NaN      NaN
# Chloe       NaN    NaN      NaN
# Danny       NaN    NaN      NaN
# Derek       NaN    NaN      NaN
# Elaine      NaN    NaN      NaN
# Eva         NaN    NaN      NaN
# Fannie      NaN    NaN      NaN
# Fred        NaN    NaN      NaN

# 为避免不重叠的位置出现NA值，可以
print(df1.add(df2,fill_value=0)) # add，sub，div，floordiv(//)整除，mul乘法，pow(**)幂次方
#         Chinese   Math  English
# Alice     247.0  278.0    248.0
# Bill      123.0  123.0    129.0
# Bob       123.0  123.0    123.0
# Carrie    130.0  132.0    122.0
# Chloe     110.0  130.0    122.0
# Danny     115.0  128.0    125.0
# Derek     113.0  124.0    121.0
# Elaine    120.0  140.0    150.0
# Eva       123.0  132.0    120.0
# Fannie    132.0  132.0    122.0
# Fred      131.0  132.0    112.0

# 默认情况下，DataFrame和Series的数学操作中会将Series的索引和DataFrame的列进行匹配，并广播到各行
import numpy as np
frame = pd.DataFrame(np.arange(12).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
series = frame.iloc[0]
print(frame)
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregon  9  10  11
print(series)
# b    0
# d    1
# e    2
print(frame-series) # 同 print(frame.sub(series))
#         b  d  e
# Utah    0  0  0
# Ohio    3  3  3
# Texas   6  6  6
# Oregon  9  9  9

# 如果想改为在行上匹配，在列上广播
series2 = frame['b']
print(series2)
# Utah      0
# Ohio      3
# Texas     6
# Oregon    9
print(frame.add(series2,axis='index')) #同 axis=0
#          b   d   e
# Utah     0   1   2
# Ohio     6   7   8
# Texas   12  13  14
# Oregon  18  19  20

# 将函数应用到一行或一列的一维数组上
f = lambda x: x.max()-x.min()
print(frame.apply(f)) # 每列调用一次
# b    9
# d    9
# e    9

print(frame.apply(f, axis='columns')) # 或：axis=1；每行调用一次
# Utah      2
# Ohio      2
# Texas     2
# Oregon    2

f2 = lambda x: '%.2f' % x
print(frame.applymap(f2))
#            b      d      e
# Utah    0.00   1.00   2.00
# Ohio    3.00   4.00   5.00
# Texas   6.00   7.00   8.00
# Oregon  9.00  10.00  11.00

print(frame['b'].map(f2))
# Utah      0.00
# Ohio      3.00
# Texas     6.00
# Oregon    9.00

# 排序和排名
df = pd.DataFrame(np.arange(8).reshape((2,4)), index=['three','one'],columns=['a','d','c','b'])
print(df.sort_index(axis=1, ascending=False))
#        d  c  b  a
# three  1  2  3  0
# one    5  6  7  4

# 加入存在NaN值，会被默认排序至底部


print(df.sort_values(by=['d','a'])) # 先按d列升序，再按a列升序
#        a  d  c  b
# three  0  1  2  3
# one    4  5  6  7

print(df.rank(axis='columns'))
#        a  d  c  b
# three  0  1  2  3
# one    4  5  6  7
print(df.rank(axis='rows'))
#          a    d    c    b
# three  1.0  1.0  1.0  1.0
# one    2.0  2.0  2.0  2.0

# 索引的is_unique属性可以告诉你他的标签是否唯一
print(df.index.is_unique) # True
# 带有重复索引的情况下，根据一个标签索引多个条目会返回一个序列，而单个条目会返回标量值

# 描述性统计
df = pd.DataFrame([[28,11,3,2],[30,4,None,2],[14,11,1,3],[22,18,4,1.2]],
                  index=['score','rebound','block','intercept'],
                  columns=['yellow','white','black','pink']) # 另一种方式创建df
print(df)
print(df.describe())
#           yellow      white     black      pink
# count   4.000000   4.000000  3.000000  4.000000
# mean   23.500000  11.000000  2.666667  2.050000
# std     7.187953   5.715476  1.527525  0.737111
# min    14.000000   4.000000  1.000000  1.200000
# 25%    20.000000   9.250000  2.000000  1.800000
# 50%    25.000000  11.000000  3.000000  2.000000
# 75%    28.500000  12.750000  3.500000  2.250000
# max    30.000000  18.000000  4.000000  3.000000

# isin方法 计算表征series中每个值是否包含于传入序列 的布尔值数组
# unique方法 计算series值中的唯一值数组，按照观察顺序返回
# value_counts方法 返回一个series，索引是唯一值序列，值是计数个数，按照个数降序排列

print(df.apply(pd.value_counts).fillna(0))
#       yellow  white  black  pink
# 1.0      0.0    0.0    1.0   0.0
# 1.2      0.0    0.0    0.0   1.0
# 2.0      0.0    0.0    0.0   2.0
# 3.0      0.0    0.0    1.0   1.0
# 4.0      0.0    1.0    1.0   0.0
# 11.0     0.0    2.0    0.0   0.0
# 14.0     1.0    0.0    0.0   0.0
# 18.0     0.0    1.0    0.0   0.0
# 22.0     1.0    0.0    0.0   0.0
# 28.0     1.0    0.0    0.0   0.0
# 30.0     1.0    0.0    0.0   0.0   

# coding=gbk

# 第六章 数据载入、存储及文件格式
import pandas as pd
import sys

# 读入文本文件
df = pd.read_excel(r'C:\Users\Ben\Desktop\testfile.xlsx','Sheet_2')
print(df)

# 将数据写入文本格式
print(df.to_csv(sys.stdout, header=False)) # 写入到sys.stdout时 可以在控制台中打印文本结果
# na_rep可以对缺失值进行标注覆盖
# index和header可以决定行列标签是否被写入

# json.loads方法可以将JSON字符串转换为Python形式
# json.dumps方法可以将Python对象转换回JSON
# pandas.read_json方法可以自动将JSON数据集按照指定次序转换为Series或DataFrame
# pandas.to_json方法可以将数据导出为JSON

import json
#print(df.to_json()) # orient='records'

# 如需将pandas数据写入到excel格式中，需要先生成一个excelwriter，然后使用pandas对象的to_excel方法将数据写入
with pd.ExcelWriter(r'C:\Users\Ben\Desktop\testfile.xlsx', mode='a') as writer:
    pd_dt = pd.DataFrame([['hello world','byebye world'],['happy day']],columns=['field one', 'field two'])
    pd_dt.to_excel(writer, 'Sheet_4', index=False)

# coding=gbk

# 第七章 数据清洗与准备
import pandas as pd

'''
处理缺失值
'''

df = pd.read_excel(r'C:\Users\Ben\Desktop\testfile.xlsx')
print(df['国家'].isnull())
# 0      False
# 1      False
#        ...
# 96     False
# 100     True

# notnull是isnull函数的反函数

# dropna默认情况下会删除包含缺失值的行
print(df.dropna(how='all')) # 传入how='all'时，将删除所有值均为NA的行
print(df.dropna(axis=1)) # 传入axis=1时，将删除包含缺失值的列
# 如果涉及时间序列数据，假设你只想保留包含一定数量的观察值的行，可以用thresh参数来表示 e.g. df.dropna(thresh=2)

# 补全缺失值
print(df.fillna('补值'))
# ...
# 99   100.0                 东风汽车公司(DONGFENG MOTOR)     84048.5   1328.4  中国
# 100     补值                              Airwallex     80000.0   1232.0  补值
# 101     补值                                   字节跳动     82456.0       补值  中国

print(df.fillna({'国家':'大中华','排名':'未知'}))
# ...
# 99   100.0                 东风汽车公司(DONGFENG MOTOR)     84048.5    1328.4   中国
# 100     未知                              Airwallex     80000.0    1232.0  大中华
# 101     未知                                   字节跳动     82456.0       NaN   中国

# fillna里，参数method 是插值方法，ffill或bfill；limit参数可以用于指定前向或后向填充时最大的填充范围
# fillna返回的是一个新的对象，如果你想修改已经存在的对象 可以使用inplace=True



'''
数据转换
'''

# 删除重复值
df = pd.DataFrame({
    'k1':['one','two'] * 3 + ['two'],
    'k2':[1, 1, 2, 3, 3, 4, 4]
})
print(df)
print(df.duplicated())
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6     True
print(df.drop_duplicates()) # 默认针对所有列
#     k1  k2
# 0  one   1
# 1  two   1
# 2  one   2
# 3  two   3
# 4  one   3
# 5  two   4

# 可以指定数据的任何子集来检测是否有重复
df['k3'] = range(7)
print(df.drop_duplicates(['k1']))
#     k1  k2  k3
# 0  one   1   0
# 1  two   1   1

# drop_duplicates默认是保留第一个观测到的值，可以传入参数 keep='last'实现返回最后一个
print(df.drop_duplicates(['k1'], keep='last'))
#     k1  k2  k3
# 4  one   3   4
# 6  two   4   6

# 使用函数或映射进行数据转换
df = pd.DataFrame({
    'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova lox'],
    'ounces':[4,3,12,6,7.5,8,3,5,6]
})
meat_to_animal = {
    'bacon':'pig',
    'pulled pork':'pig',
    'pastrami':'cow',
    'corned beef':'cow',
    'honey ham':'pig',
    'nova lox':'salmon'
}

lowercase = df['food'].str.lower() # 由于存在大小写不匹配，先将每个值都转换成小写
df['animal']= lowercase.map(meat_to_animal) # Series的map方法可以接受一个函数或一个包含映射关系的字典型对象
print(df)
#           food  ounces  animal
# 0        bacon     4.0     pig
# 1  pulled pork     3.0     pig
# 2        bacon    12.0     pig
# 3     Pastrami     6.0     cow
# 4  corned beef     7.5     cow
# 5        Bacon     8.0     pig
# 6     pastrami     3.0     cow
# 7    honey ham     5.0     pig
# 8     nova lox     6.0  salmon

df['food'].map(lambda x: meat_to_animal[x.lower()]) # Series的map方法可以接受一个函数或一个包含映射关系的字典型对象
# print(df) 打印结果同上

# 替代值
df['animal'] = df['animal'].replace({'pig':'猪','cow':'牛'})
print(df)
# 0        bacon     4.0       猪
# 1  pulled pork     3.0       猪
# 2        bacon    12.0       猪
# 3     Pastrami     6.0       牛
# 4  corned beef     7.5       牛
# 5        Bacon     8.0       猪
# 6     pastrami     3.0       牛
# 7    honey ham     5.0       猪
# 8     nova lox     6.0  salmon

# 重命名轴索引
import numpy as np
df = pd.DataFrame(np.arange(12).reshape((3,4)),
                  index=['Ohio', 'Colorado', 'New York'],
                  columns=['one', 'two', 'three', 'four'])
transform = lambda x: x[:4].upper()
df.index = df.index.map(transform)
print(df)
#       one  two  three  four
# OHIO    0    1      2     3
# COLO    4    5      6     7
# NEW     8    9     10    11

print(df.rename(index=str.title, columns=str.upper))
#       ONE  TWO  THREE  FOUR
# Ohio    0    1      2     3
# Colo    4    5      6     7
# New     8    9     10    11

df = df.rename(
    index={'OHIO': 'Indiana'},
    columns={'three': 'Unkown'}
)
print(df)
#          one  two  Unkown  four
# Indiana    0    1       2     3
# COLO       4    5       6     7
# NEW        8    9      10    11


# 连续值的离散化和分箱
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 68, 99, 41, 32, 76]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins=bins, right=False) # 用right=False来决定哪一边是封闭的
print(cats)
# [[18, 25), [18, 25), [25, 35), [25, 35), [18, 25), ..., [60, 100), [60, 100), [35, 60), [25, 35), [60, 100)]
# Length: 15
# Categories (4, interval[int64, left]): [[18, 25) < [25, 35) < [35, 60) < [60, 100)]
print(pd.value_counts(cats))
# [18, 25)     4
# [25, 35)     4
# [60, 100)    4
# [35, 60)     3


'''
字符串操作
'''
# 字符串可以用split方法拆分成多块
val = 'a,b,  guido'
print(val.split(',')) # ['a', 'b', '  guido']
print([x.strip() for x in val.split(',')]) # split常与strip一起使用，用于清楚空格和换行符
# ['a', 'b', 'guido']

# 使用符合符拼接子字符串，传入一个列表或元组
print('::'.join(['one', 'two', 'three'])) # one::two::three

# 定位子字符串
print('guido' in val) # True
print(val.find('b')) # 2
print(val.index('guido')) # 6
# find和index的差别在于：index在字符串没有找到时会抛出一个异常，而find则是返回-1

# count 返回子字符串在字符串中的非重叠出现次数
# endswith,startswith
# replace 使用一个字符串替代另一个字符串
# rfind 返回子字符串在字符串中最后一次出现时第一个字符的位置；如果没找到仍返回的是-1

# 正则表达式
import re
# re模块主要有三个主题：模式匹配，替代，拆分；  正则表达式首先会被编译，然后正则表达式的split方法在传入文本上被调用
text = 'foo  far\t  bar baz  \tqux'
print(re.split('\s+', text)) # ['foo', 'far', 'bar', 'baz', 'qux']

# 可以使用re.compile自行编译，形成一个可复用的正则表达式
regex = re.compile('\s+')
print(regex.split(text)) # ['foo', 'far', 'bar', 'baz', 'qux']

# findall方法可以帮你找到一个 所有匹配正则表达式的模式的列表
print(regex.findall(text)) # ['  ', '\t  ', ' ', '  \t']

# search返回的仅仅是第一个匹配项
text = '''Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
'''
pattern = r'[a-z0-9._%+-]+@[a-z0-9-.]+\.[a-z]{2,4}'
regex = re.compile(pattern) # flags=re.IGNORECASE
print(regex.findall(text))
# ['dave@google.com', 'steve@gmail.com', 'rob@gmail.com', 'ryan@yahoo.com']
print(regex.search(text)) # 匹配对象只能告诉我们模式在字符串中起始和结束的位置
# <re.Match object; span=(5, 20), match='dave@google.com'>
print(text[regex.search(text).start():regex.search(text).end()])
# dave@google.com

# match只在模式出现于字符串起始位置时进行匹配，如果没匹配到就会返回None
print(regex.match(text))
# None

# sub可以让原字符串中的模式被一个新字符串替代
print(regex.sub('REACTED', text))
# Dave REACTED
# Steve REACTED
# Rob REACTED
# Ryan REACTED

# 用括号将模式包起来
pattern = r'([a-z0-9._%+-]+)@([a-z0-9-.]+)\.([a-z]{2,4})'
regex = re.compile(pattern) # flags=re.IGNORECASE
print(re.findall(regex, text))
# [('dave', 'google', 'com'), ('steve', 'gmail', 'com'), ('rob', 'gmail', 'com'), ('ryan', 'yahoo', 'com')]

# sub 可以用"\1, \2"之类的特殊符号访问每个匹配对象中的分组
print(regex.sub(r'UserName: \1, Domain: \2, Suffix: \3', text))
# Dave UserName: dave, Domain: google, Suffix: com
# Steve UserName: steve, Domain: gmail, Suffix: com
# Rob UserName: rob, Domain: gmail, Suffix: com
# Ryan UserName: ryan, Domain: yahoo, Suffix: com

# pandas中的向量化字符串函数
df = {'Dave': 'dave@google.com',
      'Steve': 'steve@gmail.com',
      'Rob': 'rob@gmail.com',
      'Wes': np.nan}
print(pd.Series(df))
# Dave     dave@google.com
# Steve    steve@gmail.com
# Rob        rob@gmail.com
# Wes                  NaN

print(pd.Series(df).isnull())
# Dave     False
# Steve    False
# Rob      False
# Wes       True
print(pd.Series(df).loc[pd.Series(df).isnull()])
# Wes    NaN
print(pd.Series(df).loc[~pd.Series(df).isnull()])
# Dave     dave@google.com
# Steve    steve@gmail.com
# Rob        rob@gmail.com

print(pd.Series(df).str.contains('gmail'))
# Dave     False
# Steve     True
# Rob       True
# Wes        NaN

print(pd.Series(df).str.findall(pattern))
# Dave     [(dave, google, com)]
# Steve    [(steve, gmail, com)]
# Rob        [(rob, gmail, com)]
# Wes                        NaN

print(pd.Series(df).str.match(pattern))
# Dave     True
# Steve    True
# Rob      True
# Wes       NaN

# 可以使用字符串切片的类似于发进行向量化切片
print(pd.Series(df).str[:5])
# Dave     dave@
# Steve    steve
# Rob      rob@g
# Wes        NaN

# coding=gbk

# 第八章 数据规整：连接、联合与重塑
import pandas as pd
import numpy as np

'''
分层索引
'''
# 分层索引是pandas的重要特性，允许你在一个轴向上拥有多个索引层级
data = pd.DataFrame(np.random.randn(9), index=[['a','a','a','b','b','c','c','d','d'],
                                               [1,2,3,1,3,1,2,2,3]])
print(data)
#             0
# a 1 -0.153577
#   2 -0.155418
#   3 -0.614129
# b 1  0.555851
#   3  0.060725
# c 1 -0.553083
#   2 -0.733890
# d 2 -1.053861
#   3  1.860955

print(data['b':'c'])
#             0
# b 1 -0.720622
#   3  0.602475
# c 1 -0.928239
#   2  0.595422

print(data.loc[['b','d']])
#             0
# b 1  0.965568
#   3  0.608857
# d 2  1.311818
#   3 -0.182520

print(data.unstack())
#           1         2         3
# a  0.265800 -1.188063  0.834085
# b  0.170898       NaN  1.457887
# c -0.537320  1.075381       NaN
# d       NaN -0.581637 -0.321030

print(data.unstack().stack())
#             0
# a 1  0.331942
#   2  1.234275
#   3 -0.185384
# b 1  0.505403
#   3  0.696515z
# c 1 -0.189138
#   2 -0.325019
# d 2-2.599441
#   3  0.189821

# DataFrame中，每个轴都可以拥有分层索引
df = pd.DataFrame(np.arange(12).reshape((4,3)),
                  index=[['a','a','b','b'],[1,2,1,2]],
                  columns=[['Ohio','Ohio','Colorado'],
                           ['Green','Red','Green']])
print(df)
#      Ohio     Colorado
#     Green Red    Green
# a 1     0   1        2
#   2     3   4        5
# b 1     6   7        8
#   2     9  10       11

# 重排序和层级排序
# swaplevel接受两个层级序号或层级名称，返回一个进行了层级变更的新对象，但原数据是不变的
df.index.names = ['key1','key2']
df.columns.names = ['state','color']
print(df)
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11
print(df.swaplevel('key2','key1'))
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
# 2    a        3   4        5
# 1    b        6   7        8
# 2    b        9  10       11
print(df.swaplevel('key2','key1')['Colorado'].loc[2,'a'])
# color
# Green    5
# Name: (2, a), dtype: int32

# sort_index只能在单一层级上对数据进行排序，可以和层级变换想结合
print(df.swaplevel(0,1).sort_index(level=0))
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
#      b        6   7        8
# 2    a        3   4        5
#      b        9  10       11


'''
联合与合并数据集
'''
# pandas.merge根据一个或多个键将 行 进行连接数据集，主要用于将各种join操作算法运用在数据上
df1 = pd.DataFrame({
    'key':['b','b','a','c','a','a','b'],
    'data1':range(7)
})
df2 = pd.DataFrame({
    'key':['a','b','d'],
    'data2':range(3)
})
print(df1)
#   key  data1
# 0   b      0
# 1   b      1
# 2   a      2
# 3   c      3
# 4   a      4
# 5   a      5
# 6   b      6
print(df2)
#   key  data2
# 0   a      0
# 1   b      1
# 2   d      2
print(pd.merge(df1, df2, on='key'))
#   key  data1  data2
# 0   b      0      1
# 1   b      1      1
# 2   b      6      1
# 3   a      2      0
# 4   a      4      0
# 5   a      5      0

# 默认情况下，merge做的是内连接('inner join')，结果里的键是两张表的交集。 其他的可选项有'left', 'right', 'outer'
print(pd.merge(df1, df2, on='key', how='outer')) # 使用多个键进行合并时，传入一个列名的列表；e.g. on = ['key1', 'key2']
#   key  data1  data2
# 0   b    0.0    1.0
# 1   b    1.0    1.0
# 2   b    6.0    1.0
# 3   a    2.0    0.0
# 4   a    4.0    0.0
# 5   a    5.0    0.0
# 6   c    3.0    NaN
# 7   d    NaN    2.0


# 根据索引合并
# 某些情况下，DataFrame中用于合并的键是他的索引，这种情况下你可以传递 left_index=True或right_index=True来表示索引需要用来作为合并的键
df1 = pd.DataFrame(
    {
        'key': ['a', 'b', 'a', 'a', 'b', 'c'],
         'value':range(6)
     })
#   key  value
# 0   a      0
# 1   b      1
# 2   a      2
# 3   a      3
# 4   b      4
# 5   c      5
df2 = pd.DataFrame(
    {
        'group_val':[3.5, 7]
    },
    index=['a', 'b']
    )
#    group_val
# a        3.5
# b        7.0
print(pd.merge(df1, df2, left_on='key', right_index=True)) # left_on参数： left DataFrame中用作连接键的列
#   key  value  group_val
# 0   a      0        3.5
# 2   a      2        3.5
# 3   a      3        3.5
# 1   b      1        7.0
# 4   b      4        7.0

# 沿轴向连接
df1 = pd.DataFrame(np.arange(6).reshape(3,2), index=['a','b','c'], columns=['one','two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2,2), index=['a','c'], columns=['three','four'])
#    one  two
# a    0    1
# b    2    3
# c    4    5
#    three  four
# a      5     6
# c      7     8
print(pd.concat([df1, df2], axis=1, keys=['level_1', 'level_2'])) # 假设想在连接轴上创建一个多层索引，可以使用keys参数来实现； 不加就没有
#   level_1     level_2
#       one two   three four
# a       0   1     5.0  6.0
# b       2   3     NaN  NaN
# c       4   5     7.0  8.0
print(pd.merge(df1, df2, right_index=True, left_index=True, how='outer'))
#    one  two  three  four
# a    0    1    5.0   6.0
# b    2    3    NaN   NaN
# c    4    5    7.0   8.0

# 在DataFrame中，combine_first逐列做相同的操作，可以认为他是根据传入的对象来“修补”调用对象的缺失值
# df1.combine_first(df2) # df1有值则取df1，没有则取df2，还没有就仍为NaN


'''
重塑和透视
略
'''
# stack 堆叠 该操作会旋转或将列中的数据透视到行
# unstack 拆堆 该操作会将行中的数据透视到列

data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=['Ohio', 'Colorado'],
                    columns=['one', 'two', 'three']
                    )
#           one  two  three
# Ohio        0    1      2
# Colorado    3    4      5

data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number')
                    )
# number    one  two  three
# state
# Ohio        0    1      2
# Colorado    3    4      5
print(data.stack())
# state     number
# Ohio      one       0
#           two       1
#           three     2
# Colorado  one       3
#           two       4
#           three     5
print(data.stack().unstack())
# number    one  two  three
# state
# Ohio        0    1      2
# Colorado    3    4      5

# coding=gbk

# 第九章 绘图与可视化
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
入门
'''

# matplotlib所绘制的图位于Figure对象中，可以用plt.figure生成一个新的图片
# plt.figure有一些选项，比如figsize是确保图片有一个确定的大小以及存储到硬盘时的长宽比
fig = plt.figure()

# 不能使用空白的图片进行绘图，需要使用add_subplot创建一个或多个子图subplot
ax1 = fig.add_subplot(2,2,1)
ax1.scatter(np.arange(30), np.arange(30) + 3*np.random.randn(30))

ax2 = fig.add_subplot(222)
plt.plot(np.random.randn(50).cumsum(), 'y--') # 'y--'是用于绘制黄色分段线的style选项
ax3 = fig.add_subplot(223, facecolor='green')
plt.hist(np.random.randn(100), bins=50, color='r', alpha=0.1)
ax4 = fig.add_subplot(224, frameon=False, alpha=0.3, sharey=ax3, sharex=ax3)
plt.hist(np.random.randn(100), bins=12, color='k', alpha=0.9)

plt.subplots_adjust(wspace=0, hspace=0)

# 分割线

fig = plt.figure(figsize=(50,50))

ax1 = fig.add_subplot(2,2,1)
ds = np.random.randn(10).cumsum()
ax1.plot(ds, color='r', linestyle='dashed', marker='o', label='Default')
ax1.plot(ds, color='g', linestyle='dashed', drawstyle='steps-post', marker='o', label='steps-post')
ax1.legend(loc='best')


ax2 = fig.add_subplot(2,2,2)
ds2 = np.random.randn(20).cumsum()
ax2.plot(ds, color='r', linestyle='dashed', marker='s', label='Default')
plt.legend(loc='upper right')
ax2.set_xticks([0, 15, 20]) # 同理y轴
ax2.set_xticklabels(['zero', 'fifteen', 'twenty'])
ax2.set_xlabel('this is X axis')
ax2.set_title('MY first matplotlib plot')

ax3 = fig.add_subplot(2,2,3)
data3 = np.arange(20)
ax3.plot(data3)
ax3.set_xticks(data3)
ax3.text(10, 10, 'hello world', fontsize=6)
ax3.annotate('some words',
             xy=(15,15), # 箭头指向的位置
             xytext=(15,19), # 文字的位置，也是箭头的起始位置
             arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4),
             horizontalalignment='left',
             verticalalignment='top'
             )

plt.savefig(r'C:\Users\Ben\Desktop\plt_file02.pdf')

# coding=gbk

# 第十章 数据聚合与分组操作
import pandas as pd
import numpy as np

'''
Groupby机制
'''

df = pd.DataFrame(
    {
        'key1': ['a', 'b', 'b', 'a', 'b'],
        'key2': ['one', 'two', 'one', 'two', 'one'],
        'data1': np.arange(5),
        'data2': [12, 32, 43, -12, 123]
    }
)

df['data1'].groupby([df['key1'], df['key2']]).mean()
# key1  key2
# a     one     0.0
#       two     3.0
# b     one     3.0
#       two     1.0

df.groupby(['key1', 'key2']).mean()
#            data1  data2
# key1 key2
# a    one     0.0   12.0
#      two     3.0  -12.0
# b    one     3.0   83.0
#      two     1.0   32.0

df.groupby(['key1']).mean() # 结果里并没有key2列，因为df['key2']并不是数值数据，即df['key2']是一个冗余列，并排除在了结果之外
#          data1  data2
# key1
# a     1.500000    0.0
# b     2.333333   66.0

df.groupby(['key1', 'key2'])['data1'].sum()
# key1  key2
# a     one     0
#       two     3
# b     one     6
#       two     1

df.groupby(['key1', 'key2'])[['data1']].sum()
#            data1
# key1 key2
# a    one       0
#      two       3
# b    one       6
#      two       1

# 可以使用函数分组
df.set_index(pd.Index(['thomas', 'james', 'ben', 'james', 'durant']), inplace=True)
#        key1 key2  data1  data2
# thomas    a  one      0     12
# james     b  two      1     32
# ben       b  one      2     43
# james     a  two      3    -12
# durant    b  one      4    123

df.groupby(len).sum()
#    data1  data2
# 3      2     43
# 5      4     20
# 6      4    135

# 根据层级分组时，可以将层级数值或层级名称传递给level关键字

'''
数据聚合
'''

df = pd.DataFrame(
    {'data1': [1, 2, 3, 4],
     'data2': [11, 22, 33 ,44],
     'key1': ['a', 'b', 'b', 'a'],
     'key2': ['one', 'one', 'two', 'three']
     }
)
#    data1  data2 key1   key2
# 0      1     11    a    one
# 1      2     22    b    one
# 2      3     33    b    two
# 3      4     44    a  three

# 如果想使用自己的聚合函数，需要将函数传递给aggre或agg方法
def peak2peak(arr):
    return (arr.max()) ** 2

df.groupby(['key1']).agg(peak2peak)
# FutureWarning: Dropping invalid columns in SeriesGroupBy.agg is deprecated. In a future version, a TypeError will be raised. Before calling .agg, select only columns which should be valid for the aggregating function.
#   results[key] = self.aggregate(func)
#       data1  data2
# key1
# a        16   1936
# b         9   1089

df.groupby(['key1','key2'])['data2'].agg([peak2peak, 'mean'])
#             peak2peak  mean
# key1 key2
# a    one          121  11.0
#      three       1936  44.0
# b    one          484  22.0
#      two         1089  33.0

df = pd.DataFrame({
    'key': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'data': [0, 5, 10, 5, 10, 15, 10, 15, 20]
})
#   key  data
# 0   A     0
# 1   B     5
# 2   C    10
# 3   A     5
# 4   B    10
# 5   C    15
# 6   A    10
# 7   B    15
# 8   C    20

# groupby方法最常见的应用是apply，apply将对象拆分成多块，然后在每一块上调用传递的函数，之后尝试将每一块拼接到一起
def top(arr, n=2, column='data'):
    return arr.sort_values(by=column)[-n:]

df.groupby(['key']).apply(top)
#       key  data
# key
# A   3   A     5
#     6   A    10
# B   4   B    10
#     7   B    15
# C   5   C    15
#     8   C    20

df.groupby(['key']).apply(top).unstack()
#      key                          data
#        3    4    5    6    7    8    3     4     5     6     7     8
# key
# A      A  NaN  NaN    A  NaN  NaN  5.0   NaN   NaN  10.0   NaN   NaN
# B    NaN    B  NaN  NaN    B  NaN  NaN  10.0   NaN   NaN  15.0   NaN
# C    NaN  NaN    C  NaN  NaN    C  NaN   NaN  15.0   NaN   NaN  20.0

'''
数据透视表 - 为groupby提供一个方便接口，还可以添加部分总计，也称作边距。【这个功能也可以直接使用groupby实现】
'''
df['data1'] = df['data']*2
df['data2'] = [1,2,3,4,5,6,7,8,9]
df['tag'] = ['M', 'F', 'M', 'M', 'M', 'M', 'F', 'M', 'F']
#   key  data  data1  data2 tag
# 0   A     0      0      1   M
# 1   B     5     10      2   F
# 2   C    10     20      3   M
# 3   A     5     10      4   M
# 4   B    10     20      5   M
# 5   C    15     30      6   M
# 6   A    10     20      7   F
# 7   B    15     30      8   M
# 8   C    20     40      9   F

# 可以通过传递margins=True来扩充这个表来包含部分总计，这会添加 All行 和 列标签，其中相应的值就是单层中所有数据的分组统计值
# 要使用不同的聚合函数时，将函数传递给aggfunc
# 如果某些情况下产生了空值或NA，可以传递一个fill_value
df.pivot_table(['data1', 'data2'], index=['tag'], columns=['key'], aggfunc=sum, margins=True)
#     data1              data2
# key     A   B   C  All     A   B   C All
# tag
# F      20  10  40   70     7   2   9  18
# M      10  50  50  110     5  13   9  27
# All    30  60  90  180    12  15  18  45

# coding=gbk

# 第十一章 时间序列
import pandas as pd
import numpy as np
import datetime
import dateutil

'''
日期和时间数据的类型和工具
'''

# datetime.strptime是在已知格式的情况下转换日期的好方式，但缺点是每次都要手动编写格式代码
# dateutil能够解析大部分人类可理解的日期表示，但也不是完美的，会存在误识别
dt = dateutil.parser.parse('11/12/2023', dayfirst=True) # 可以传递dayfirst来表明日期出现在月份之前
# 2023-12-11 00:00:00
type(dt) # <class 'datetime.datetime'>

# 无论是用作轴索引还是用作Dataframe中的列，pandas的to_datetime方法可以转换很多不同的日期表示格式
# 可以处理缺失值，如None，空字符串等
datestrs = ['2022-07-06 12:00:00', '2020-12-31 08:00:00', None]
pd.to_datetime(datestrs)
# DatetimeIndex(['2022-07-06 12:00:00', '2020-12-31 08:00:00', 'NaT'], dtype='datetime64[ns]', freq=None)
# NaT Not a Time， 是pandas中时间戳数据的null值表现形式


'''
时间序列基础
'''

datestrs = ['2022-07-06 12:00:00', '2020-12-31 08:00:00']
df = pd.DataFrame(
    {
        'data': [13, 15]
    },
    index= datestrs
)
#                      data
# 2022-07-06 12:00:00    13
# 2020-12-31 08:00:00    15

df + df[:1] # 不同索引的时间序列之间的算术运算在日期上可以自动对齐
#                      data
# 2020-12-31 08:00:00   NaN
# 2022-07-06 12:00:00  26.0

long_ts = pd.DataFrame(
    {
        'data': np.arange(10)
    },
    index=pd.date_range('2000-10-10', periods=10)
)
#             data
# 2000-01-01     0
# 2000-01-02     1
# 2000-01-03     2
# 2000-01-04     3
# 2000-01-05     4
# 2000-01-06     5
# 2000-01-07     6
# 2000-01-08     7
# 2000-01-09     8
# 2000-01-10     9

long_ts.loc['2000-10-12':'2000-10-14':2]
#             data
# 2000-10-12     2
# 2000-10-14     4

long_ts.loc['2000'] # 会被解释为一个年份，然后输出相应的时间区间

# 含有重复索引的时间序列
df = pd.DataFrame(
    {'data': [10, 20, 30, 40, 11, 25]},
    index=pd.DatetimeIndex(['2022-01-01', '2022-01-02', '2022-01-02', '2022-01-02', '2022-01-04', '2022-01-04' ])
)
#             data
# 2022-01-01    10
# 2022-01-02    20
# 2022-01-02    30
# 2022-01-02    40
# 2022-01-04    11
# 2022-01-04    25

df.index.is_unique # 判断索引是否唯一
# False

df.groupby(level=0).sum()
#             data
# 2022-01-01    10
# 2022-01-02    90
# 2022-01-04    36

'''
日期范围 频率 移位
'''

# pandas.date_range是用于根据特定频率生成指定长度的DatetimeIndex
pd.date_range('2022-02-13', periods=6, freq='M') # 如果没有指定freq，则默认为日 ‘D’
# DatetimeIndex(['2022-02-28', '2022-03-31', '2022-04-30', '2022-05-31',
#                '2022-06-30', '2022-07-31'],
#               dtype='datetime64[ns]', freq='M')

# 如果想生成的是标准化为零点的时间戳，可以传normalize=True

pd.date_range('2022-02-13', periods=6, freq='2H30min')
pd.date_range('2022-02-13', periods=6, freq=pd.tseries.offsets.Hour(4)+pd.tseries.offsets.Minute(20))
# DatetimeIndex(['2022-02-13 00:00:00', '2022-02-13 04:20:00',
#                '2022-02-13 08:40:00', '2022-02-13 13:00:00',
#                '2022-02-13 17:20:00', '2022-02-13 21:40:00'],
#               dtype='datetime64[ns]', freq='260T')

# 允许你获取诸如 每月第三个星期五 这样的日期，通过传输 freq='WOM-3FRI'

# 移位 是指将日期按照时间向前或向后移动，但 不改变索引

df = pd.DataFrame(
    {'data': [20, 40, 60, 55, 90]},
    index=pd.date_range('2020-12-15', freq='W', periods=5)
)
#             data
# 2020-12-20    20
# 2020-12-27    40
# 2021-01-03    60
# 2021-01-10    55
# 2021-01-17    90

df.shift(3).fillna(10) # 这里的3是和你先前定义传输的freq相呼应的，正数表示将数据往后(晚)平移
#             data
# 2020-12-20  10.0
# 2020-12-27  10.0
# 2021-01-03  10.0
# 2021-01-10  20.0
# 2021-01-17  40.0

df/df.shift(1) - 1 # 可以用来反映多列时间序列的百分比变化
#                 data
# 2020-12-20       NaN
# 2020-12-27  1.000000
# 2021-01-03  0.500000
# 2021-01-10 -0.083333
# 2021-01-17  0.636364

# shift里仍可以定义freq，为前移后移提供灵活性
