# 1.一个类可以创建多个对象 2.多个对象调用函数的时候 self地址是否相同? (不相同)
class washer():
    def wash(self):
        print('洗衣服')
        print(self)
heier1 = washer()
heier1.wash()

heier2 = washer()
heier2.wash()
