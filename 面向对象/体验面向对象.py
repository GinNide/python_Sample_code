# 需求 洗衣机 功能 洗衣服
# 1. 定义洗衣机类
'''
class 类名():
    代码
'''

class water():
    def wash(self):
        print("能洗衣服")


# 2.创建对象
#　对象名　＝　类名（）
haier = water()


# 3.验证成果
# 打印haier这个对象
print(haier)

# 使用wash 功能 -- 实例方法/对象方法  对象名.wash()
haier.wash()