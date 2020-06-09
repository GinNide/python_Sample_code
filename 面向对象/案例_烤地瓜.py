# 定义类 初始化属性  焙烤和添加调料的方法 显示对象的信息的str
class SweetPotato():
    #def __int__(self):
    def __init__(self):    # 注意是init 不是int
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        # 1. 计算烤地瓜整体烤过的时间
        self.cook_time += time       # 累加时间 才能进行条件判断
        # 2. 用整体烤过的时间在去判断地瓜的状态
        if 0 <= self.cook_time < 3:
            # 生的
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            # 半生不熟
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            # 熟了
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            # 烤糊了
            self.cook_state = '烤糊了'
    def __str__(self):
        return f'这个地瓜的被烤过的时间是{self.cook_time}, 状态是{self.cook_state}'
# 创建对象并调用出对应的实例方法
digua1 = SweetPotato()

print(digua1)

digua1.cook(2)

print(digua1)

digua1.cook(2)

print(digua1)
