#　定义两个函数
def test1():
    return  50


def test2(num):
    print(num)

# 先得到函数1的返回值
age = test1()
# print(age)

test2(age)   # 返回值作为参数 传入另外一个函数

