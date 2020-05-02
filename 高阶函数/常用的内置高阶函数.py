# map()
# 语法 map(func, lst) 将传入的函数变量func作用到lst变量的每个元素中，并将结果组成的迭代器返回
# list1 = [1,2,3,4,5,]  # 准备数据


# def func(x):   # 定义函数 实现二次方计算
#     return x ** 2


# age = map(func,list1)  #调用函数
# print(age)   # 迭代器打印出来是内存地址
# print(list(age))  # 用list去转换成列表  然后用print打印出来


# reduce(func,lst)  其中func必须有两个参数 每次func计算的结果继续和序列的下一个元素做累加计算
# reduce() 传入的参数func必须结束2个参数


# import functools   # reduce（）的必需品
# list1 = [1,2,3,4,5,]  # 列表数据
#
# def func(a,b):
#     return a + b
#
# age = functools.reduce(func,list1)    #　前面是函数名　后面是列表数据　　reduce 需要两个参数
# print(age)


# filter
# filter(func,lst),函数用于过滤序列过滤掉不符合条件的元素,返回一个filter对象。如果要转换为列表可以用list（）去转换
list1 = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x % 2 == 0    # 取偶数
age = filter(func,list1)
print(age)
print(list(age))