# 函数去实现 a + b
def add(a,b):
    return a + b
message = add(10,20)
print(message)

# lambda实现 a + b
fn1 = lambda a,b : a + b   # 给个变量 方便调用
print(fn1(10,20))                # 写法大致一样
# 打印变量 看到返回值