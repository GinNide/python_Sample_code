a = 100

print(a)


def testA():
    print(a)


def testB():
    global a  # 声明a为全局变量   global 可以声明
    a = 200  # 局部变量  这是testB 定义的一个局部变量
    print(a)


testA()
testB()

print(a)


# 直接在函数里面修改 a 的变量这个不是全局变量 而是局部变量
# global 可以声明 修改后的  a 为全局变量