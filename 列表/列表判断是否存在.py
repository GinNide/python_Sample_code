name = ['dsl','sssdd','sadwf']

# 注册邮箱 用户给一个用户名 如果存在 提示可以注册 反之 取反

name1 = input('请输入邮箱名字')
if name1 in name:
    print(f"你输入的名字是{name1},该用户已经存在")
else:
    print(f"你输入的名字是{name1},可以注册")
    # f进行格式化输出会显得很工整