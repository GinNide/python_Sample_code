# 在python中 __xx__()的函数叫做魔法方法 指的是具有特殊功能的函数
# _init_() 初始化对象

# 目标： 定义init 魔法方法设置初始化属性 并访问调用

'''
1. 定义类
init 魔法方法 ： width height
添加实例属性 访问实例属性

2. 创建对象
3. 验证结果
调用实例方法
'''

class washer():
    def __init__(self):
        # 添加实例属性
        self.width = 100
        self.height = 200
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

# 创建对象
haier = washer()

#　验证结果
haier.print_info()