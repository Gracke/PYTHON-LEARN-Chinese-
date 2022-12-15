"""
集合
   集合具有无序性(当set输出时，输出元素会随机排序，唯一性，用于元组或者列表
1.元素是唯一的，用于数组的去重
2.变量名= set() 字符/元组/列表/字典
3.变量名= {元素， 元素， ， ， } ---(元组/字符/数字)>不可变类型
"""
# 字符串（随机排列）
# r = set("1234")
# print(r)
# 元组（不会随机排列）因为元组本身是不可变的
# s = set((1, 2, 3, 4))
# print(s)

# 列表（不会随机排列）
# d = set([1, 2, 3, 4])
# print(d)

# 字典（会随机排列）
# c = {'名字': '不吃鱼',
#      '年龄': 18
#      }
# print(set(c))  # {'名字', '年龄'}

# 创造集合--元组/字符/数字，不能使用列表/字典
# v = {1, 2, 3, ('我'), '你'}
# # print(v)

"""集合去重"""
# 字符串
# k = set('哇哇哇哇哇哇了的')
# print(k)

# 元组
# x = set((1, 1, 1, 2, 3))
# print(x)

# 列表
# z = set(['不吃鱼', '不吃鱼', 1, 2])
# print(z)

# 每一种数组都为一个整体
# l = {1, 2, 2, '1, 2, 2'}
# print(l)

"""
集合的添加与合并
1.add--集合末添加元素,不能用列表
2.update--集合的合并
"""
a = {1, 2, 3, 4}
b = {99, 66, '尼卡'}
# a.add(6)
# a.add('包菜')
# a.add((11, 22,))
# print(a)

# 随机排列（被合并的集合进行改变）
# a.update(b)
# print(a)

"""
集合的删除元素的方法
1.remove
2.pop
3.discard
"""
e = {'airport', 11, 22, (11, 22)}
# remove-括号内不能为空集(否则会报错),输入相对应的值，返回删除后的列表
# e.remove(11)
# print(e)


# pop-括号为空集，但是会随机删除
# e.pop()
# print(e)

# discard-输出不存在的数值时，discard不会报错(返回相对位置)
e.discard(1)
print(e)


"""集合的交集与并集
1.交集-&,输出两集合的相同元素
2.并集-|，输出两集合的所有数据
"""
m = {1, 2, 3}
n = {3, 1, 6}
x1 = m & n
x2 = m | n
print(x1)
print(x2)
