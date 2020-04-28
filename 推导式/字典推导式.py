# 创建字典  键是1-5  
# dict1 = {i: i**2 for i in range(1,6)}
# print(dict1)

# list1 = ['name','age','gender']
# list2 = ['tom',20,'man']
# dict1 = {list1[i]: list2[i] for i in range(len(list1))}
# print(dict1)

#  如果两个列表数据个数相同，len统计任何一个列表数据都可以
#  如果两个列表数据个数相同，len统计数据多的会报错 要len数据少的
#　根据下标进行匹配

# if 条件判断

c1 = {'dl':268,'hp':125,'lx':201,'acer':99}
# 获取所有键值对数据 判断v值大于200
# print(c1.items())
dict1 = {value for value in c1.values() if value >= 200}
print(dict1)
