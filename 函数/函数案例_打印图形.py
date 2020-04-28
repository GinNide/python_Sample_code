def bar():            # 先打印一条横线
    print('-' * 20)


bar()

def digital(num):
    i = 0
    while i < num:
        bar()
        i += 1

digital(10)