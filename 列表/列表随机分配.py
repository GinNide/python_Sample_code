# 8个老师 3个办公室 将八个老师随机分配到3个办公室
import random
teacher = ['a','b','c','d','e','f','g','h']  # 老师人数
office = [[], [], []]   # 办公室人数 空列表等待接收数据
for name in teacher:
    num = random.randint(0,2)     # 取随机数 0 1 2
    office[num].append(name)
# print(office)
for i in office:
    print(f"办公室的人数{len(office)},老师分别是")
    for name in i:
        print(name)
