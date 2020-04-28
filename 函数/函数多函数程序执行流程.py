glo_num = 0

def test1():
    global glo_num
    glo_num = 100



def test2():
    print(glo_num)

print(glo_num)  # 0 修改的函数并没有执行
test2()         # 0 修改的函数，没执行
test1()
test2()         #　100 调用函数2
print(glo_num)  #  100 全局变量已经修改
