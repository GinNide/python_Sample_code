# 无参数
# fn1 = lambda : 100
# print(fn1())


# 一个参数
# fn2 = lambda a:a
# print(fn2('hello world'))


# 默认参数(缺省参数)
# fn3 = lambda a, b, c=100 : a + b + c   # 默认参数给不给没关系  如果传了实参数据就覆盖 默认值  如果没有给实参就使用默认值
# print(fn3(100,200))                    # 和函数中无差别


# 可变参数 *args
# fn4 = lambda *args: args  #　args理论上用什么都行  但是推荐使用args
# print(fn4(10,20,30))  # 返回一个元组 可以接收更多的数据
# print(fn4(10,40,4,5,51,5,45,500,5))
# print(fn4(5))  # 即使只有一个数据  元组数据后面也会有逗号


# 可变参数 **kwargs
# 返回不定长度的关键字参数
fn5 = lambda **kwargs : kwargs
print(fn5(age=15,layad= "name"))      #  key = values
# 收集关键字参数返回字典

