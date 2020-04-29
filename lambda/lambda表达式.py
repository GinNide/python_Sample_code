# lambda 参数列表 : 表达式
# lambda 的表达的参数可有可无 函数的参数在lambda表达式中完全适用
# lambda 表达式能接受任何数量的参数 但是 只能返回一个表达式的值


# 函数实现
# def fn1():
#     return 100
# age = fn1()
# print(age)


# lambda 实现        lambda表达式 叫做 匿名函数
fn2 = lambda : 100
print(fn2)   # 返回lambda的内存地址
print(fn2())  # 打印lambda表达式调用

# lambda 节省函数的代码量  (只有一个返回值的时候）