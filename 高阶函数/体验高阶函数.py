# 高阶函数
# 把函数作为参数传入 这样的函数称为高阶函数 高阶函数是函数式编程的体现
# 函数式编程就是指这种高度抽象的编程范式


# abs() 求绝对值计算
# print(abs(-10))
# round() 可以完成小数的四舍五入
# print(round(1.2))
#
#
# 写法
# def add_num(a,b):
#     return abs(a) + abs(b)   # 求 a 和 b 的绝对值累加和
# age = add_num(-1.45,66)
# print(age)

def sum_num(a,b,c):
    return c(a) + c(b)
age = sum_num(-10,255,abs)   # 把abs函数当参数输入
print(age)


def sum_num(a,b,c):
    return c(a) + c(b)
age = sum_num(-10,255.5,round)   # 把round函数当参数输入
print(age)