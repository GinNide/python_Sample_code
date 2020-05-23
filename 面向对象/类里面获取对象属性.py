# 语法 self.属性名

# 定义类
class washer():
    def wash(self):
        print('洗衣服')

    # 定义对象属性
    def print_info(self):
        # print(self.width)
        # print(self.height)
        print(f'洗衣机的宽度{self.width}')
        print(f'洗衣机的高度{self.height}')

# 创建对象
haier = washer()


# 添加实例属性
haier.width = 100
haier.height = 1000

# 结果
haier.print_info()