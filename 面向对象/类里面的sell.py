# 类：洗衣机 功能：洗衣服
class washer():
    def wash(self):
        print('洗衣服')
        print(self)

tiane = washer()
tiane.wash()
# 由于打印对象和打印self得到的内存地址相同所以self指的是调用该函数的对象
