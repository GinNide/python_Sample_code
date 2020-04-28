#* ' + '和' * '不支持字典类型
#* 在容器里面 ' + ' 起到合并的作用

# age1 = 'aa'
# age2 = 'bb'
# print(age1 + age2)

#*  字符串 元组 列表 用法类似
#* 字典是不支持的

#*  ' * '
#*   ' * '在容器里面起到的是复制的作用 
# print('-' * 10) 


#*  in   判断元素是否存在
#*  not in 判断元素是否不存在 

#* 在字典 和 元组 列表 字符串里都可使用


#* len()   计算容器中的个数
#* del()   删除 
#* max()  返回元素最大值
#* min()  返回元素最小值
#* range(start,end,step)      开始 结束 步长 
#* 生成star到tend step为步长 供for循环使用
# print(range(1,10,1))
# for i in range(1,10,1):
#     print(i)
# for i in range(1,10,):
#     print(i)
# for i in range(1,10,2):
#     print(i)
# for i in range(10):
#     print(i)

#  如果不写开始 默认0开始
#  如果不写步长 默认为1

# enumerate(可遍历对象，star = 0) 
# enumerate 返回的结果是元组 元组第一个数据是可迭代数据对应的索引，第二个是数据
lsds = ["0",'4','6','8']
# for i in enumerate(lsds):
#     print(i)  

for i in enumerate(lsds,start = 1):    # start默认为0 可以自己设置 元组第一个数据以start开始
    print(i)