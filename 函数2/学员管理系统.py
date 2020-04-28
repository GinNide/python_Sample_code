# 系统简介
# 添加学员
# 删除学员
# 修改学员信息
# 查询学员信息
# 显示所有学员信息
# 退出系统
# --------------------------------------------


# 2020 4-27
# by == 林祈

# 系统功能循环使用 直到用户输入6 才执行退出
# 0 定义功能界面函数


# 等待存储数
info = []

# 添加学员信息
def add_info():
    '''添加学员函数'''
    # 1 用户输入 姓名 手机号 学号
    new_id = input('请输入学号')
    new_name = input('请输入姓名')
    new_tel = input('请输入手机号')
    # 判断是否添加这个学员 如果学员姓名存在报错 不存在就添加
    global info
    # 不允许姓名重复 判断用户输入的姓名 是否和列表中字典的name所对应的值 是否相同
    for i in info:
        if new_name == i['name']:
            print('用户输入的姓名已经存在')
            return  # 退出当前的函数 让后面添加信息的代码不执行
    for a in info:
        if new_id == a['id']:
            print('用户输入的学号已经存在')
            return
    for b in info:
        if new_tel == b['tel']:
            print("用户输入的手机号已经存在")
            return


# 准备空字典 添加数据
    info_dict = {}
    # 字典新增数据
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    # 列表追加新字典
    info.append(info_dict)
    print(info)


# 删除学员
def del_info():
    '''删除学员'''
    # 用户输入要删除的学员姓名
    del_name = input('请输入你要删除的学员名字')
    global info  # 声明 info 为全局变量
    for i in info:
        if del_name == i['name']:
            info.remove(i)    #　 remove删除
            print('已删除')
            break
    else:
        print('你输入的用户不存在')
    print(info)

# 修改学员信息
def modify_info():
    modify_tel = input('请输入学员姓名')
    global info
    for i in info:
        if modify_tel == i["name"]:
            i['tel'] = input('请输入新的手机号:')
            break
    else:
        print('你输入的用户名不存在')

    for a in info:
        if modify_tel == i['name']:
            i['id'] = input('请输入新的学号:')
            break
    else:
        print('你输入的用户名不存在')

    print(info)


# 查找学员信息
def sarch_info():
    sarch_information = input('请输入学员的名字')
    global info
    for i in info:
        if sarch_information == i['name']:
            print(f"学员的学号是{i['id']},学员的手机号是{i['tel']}")
            break
    else:
        print('你输入的用户名不对')


def info_print():
    print('请选择功能--------------')
    print('1-添加学员')
    print('2-删除学员')
    print('3-修改学员信息')
    print('4-查询学员信息')
    print('5-显示所有学员信息')
    print('退出系统')
    print('-' * 20)



# 1 显示功能界面
while True:
    info_print()


    # 用户输入功能序号
    user_num = int(input('请输入功能序号：'))


    # 按照用户输入的功能序号 执行不同的功能
    # 用多重判断
    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        sarch_info()
    elif user_num == 5:
        print('显示所有学员信息')
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('输入的功能序号有误')