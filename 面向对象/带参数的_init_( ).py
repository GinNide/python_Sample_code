# 定义类 带参数的init： 宽度和高度     实例方法： 调用实例属性
class washer():
    def __init__(self,width,height):    # 两个形参  init 不要程序员手动调用 会自己调用
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度{self.width}')
        print(f'洗衣机的高度{self.height}')


# 创建多个对象 且实例属性不同  调用实例方法
haier = washer(555,5885)
haier.print_info()

# 如果没有参数就会报错
haier1 = washer(656,5655)
haier1.print_info()