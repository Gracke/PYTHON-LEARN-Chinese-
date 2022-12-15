"""
1.转义符： \
2.换行： \n
3制表符： \t
4.覆盖： \r
5.删除： \b
6./: 两个代表一个
7.前缀R与r在使转义符不起作用
"""
# print('我的名字\'芥兰\'不吃鱼')

# print('我的名字\r芥兰不吃鱼')

# print(r'我的名字\n芥兰不吃鱼')


# python的空值以及内置函数的返回值--none
# r = print("12345")
# print(r)

# 字符串-切片
# 切片 ([开始:结尾])
# name = '我是芥兰不吃鱼'
# print(name[-3:])

# 切片([开始:结尾:步长])
# name = '以前可难见到g2的教科书式爆弹'
# print(name[1:9:2])

s = '芥兰不吃鱼'
# print(s[0])

print('----------------------------------------------------')

"""
加法   +
乘法   *
剪发   -
除法   /
整除取整  // 
两个数取余的数 %
幂运算 ** 谁是谁的几次方
"""
"""
比较运算符
    > 大于
    < 小于
    <= 大于等于
    <= 小于等于
    != 不等于
    == 等于
    true = 1
    false = 0
与或否运算符
    与 and 
    否 not
    或 or
"""
# 数值运算
print(6 // 4)
# print(6 % 4)
# print(2 ** 2)

print('----------------------------------------------------')

"""
in & to-是检测对象是否具有该对象的序列成员
1.in - 若序列(字符串/列表/元祖/字典)中存在相应的成员，则返回true，否则返回false
2.not in - 若不存在序列，则返回true
"""
# print('我' in '我你他')
# print(1 in (1, 2, 3, 4))
# print(2 in [1, 2, 4, 6])
# print('年龄' in {'年龄' : '18'})
#
# print('i' not in 'i love you')

"""
is&not in-检测对象是否相同
"""
# a1 = '李峋'
# a2 = '李峋'
# print(a2 is a1)
#
# b1 = (1,2,3,4)
# b2 = (1,2,3,4)
# print(b1 is b2)
#
# c1 = 1,2,3,4
# c2 = 1,2,3,4
# print(c1 is c2)

d1 = {'年龄' : '18',
      '性别' : '男'
      }
d2 = {'年龄' : '18',
      '性别' : '男'
      }
print(d1 is d2)

f1 = [1, 2, 3, 4]
f2 = [1, 2, 3, 4]
print(f1 is f2)

g1 = {1,2,3,4}
g2 = {1,2,3,4}
print(g1 is g2)

print('----------------------------------------------------')



# 字符串的拼接-join
# a = '我的名字'
# b = '不吃鱼'
# c = '芥兰'
# f = ','. join((a,b,c))
# print(f)

print('----------------------------------------------------')

"""字符串的常用方法"""
s1 = 'vitality是epl冠军'
s2 = 'asd1fgh1jkl'
s3 = '      g2有hoxxi是真的强          '
s4 = '66666champion666666'

# find & count
# print(s1.find('i',1,))     # 寻找目标字符的位置，若不存在，则返回-1
# print(s1.count('l',1,))    # 统计目标字符的出现的数目

# replace & upper & lower
# print(s1.replace('epl冠军','champion of epl'))     # 替换的基本函数
# print(s1.replace('i','s',1))                         # 只替换规定位置的字符(包括空格符)，默认情况是全部替换
# print(s1.upper())  # 将字母小写转化为大写
# print(s1.lower())  # 将字母大写转化小写

# split & strip
print(s2.split('1', 1))  # 以规定的字符'1'进行分割。分割'1'次
print(s3.strip())  # 去除"首尾"'空格符号'
print(s4.strip('6'))  # 去除首尾'6'

print('----------------------------------------------------')

# 传统的格式化输出&表达式
"""
  %s为字符型格式化输出-所有字符
  %d为数值型格式化输出-整数型(若有小数点，则取整)                                                                                                                       
  %f为浮点数格式输出-小数型
  F表达式  
 """
print('我%s你' % '爱')
print('成绩%d' % 99.99)
print('成绩%f' % 99.99)
# 表达式--one(format普通表达)
y1 = '芥兰'
y2 = '男'
y3 = '20'
y4 = '名字{},性别{}，年龄{}'
# print(y4.format(y1, y2, y3))
# 表达式--another
f1 = '西谷夕'
f2 = '160.5 cm'
f3 = f'名字{f1},身高{f2}'  # 注意前面有个'f'字符
# print(f3)

print('----------------------------------------------------')

"""
format其他用法
len() - 字符串的长度
format
1.格式化小数长度(四舍五入)--- :.(格式化的小数点的位数)f
2.将小数化为百分数------:.(格式化的小数点的位数)%
"""
print(len('python'))
p1 = 3.1415926
print('今天的水果是{:.2f}斤'.format(p1))   #保留两位小数
print('今天的水果是{:.2%}斤'.format(p1))   #保留两位小数,并化为百分数

# 字符串的格式化-format
# print("名字芥兰 性别男 爱好排球")
# s2 = '名字{}.性别{}.爱好{}'
# print(s2.format('芥兰','男','排球'))

print('----------------------------------------------------')

"""字符串的编码与解码"""
# 编码
g = '数字是什么'
code_GBK = g.encode('GBK编译规则')
print(code_GBK)
code_UTF8 = g.encode('utf-8')
print(code_UTF8)
# 解码
print(bytes.decode(code_UTF8,'utf-8'))
print(bytes.decode(code_GBK,'gbk'))

print('----------------------------------------------------')

"""eval函数"""
# 1.eval无参实现字符串转化
s = '1+2+3*5-2'
print(eval(s))  # 16

# 2.字符串中有变量也可以
x = 1
print(eval('x+2'))  # 3

# 3.字符串转字典
print(eval("{'name':'linux','age':18}"))
# 输出结果：{'name':'linux','age':18}

# 4.eval传递全局变量参数,注意字典里的:age中的age没有带引号，说明它是个变量，而不是字符串。
# 这里两个参数都是全局的
print(eval("{'name':'linux','age':age}", {"age": 1822}))
# 输出结果：{'name': 'linux', 'age': 1822}
print(eval("{'name':'linux','age':age}", {"age": 1822}, {"age": 1823}))
# 输出结果：{'name': 'linux', 'age': 1823}

# eval传递本地变量，既有global和local时，变量值先从local中查找。
age = 18
print(eval("{'name':'linux','age':age}", {"age": 1822}, locals()))
# 输出结果：{'name': 'linux', 'age': 18}
print("-----------------")

print(eval("{'name':'linux','age':age}"))