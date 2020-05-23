# 语法 对象名.属性名
class washer():
    def wash(self):
        print('洗衣服')

haier1 = washer
# 添加属性
haier1.width = 100
haier1.height = 500

# 获取属性
print(f'洗衣机的宽度{haier1.width}')
print(f'洗衣机的高度{haier1.height}')
