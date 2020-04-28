# 位置参数
#  传递和定义参数的顺序和个数是必须一致
#
# def user_info(name,age,gender):
#     print(f'你的姓名是{name},年龄是{age},性别是{gender}')    # f进行 格式输出
# user_info('dsl',18,'男') # 少一个实参就会报错
#                          #  顺序也和定义必须一致 否则导致数据无意义

# 关键字参数
# 函数调用 通过 键 = 值 的形式去指定

# def user_info(name, age, gender):
#     print(f'你的姓名是{name},年龄是{age},性别是{gender}')


# user_info('dsl', age=18, gender='男')
# user_info('xiaoming', gender='女', age=28)  # 关键字没有先后书写顺序   但是位置参数必须写在关键字参数前面


# 缺省参数
# 缺省参数又叫默认参数 用于定义函数 为参数提供默认值

def user_info(name,age,gender='男'):
    print(f'你的姓名是{name},年龄是{age},性别是{gender}')
user_info('dsl',18)   # 默认参数不给实参 就用默认值
user_info('toe',19,gender='女')   #　传值了　就使用这个实参　修改了默认值
user_info('lit',18)
