# def buy():
#     return "烟"
#     print(0)            #  不执行 直接跳过
# gus = buy()
# print(gus)

# return 返回给函数调用的地方
# return 函数返回值
# return  遇到return 退出当前函数 return 后的代码都不会执行

def return1():
   # return 1,2
   # return 后可以直接写列表 字典 元组 返回多个值
   return [3,5,8,5,8]
   # 其他类型 照葫芦画瓢
requeste = return1()
print(requeste)  # 输出的是一个元组