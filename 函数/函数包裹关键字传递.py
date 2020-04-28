# 包裹关键字传输
def user_info(**kwargs):   # 最好用kwargs  作为名字
    print(kwargs)

user_info(name='tom',age=18,gerden='man')   # 形参名字不能加 引号

# 无论是包裹位置传递还是包裹关键字传递  都是一个组包的过程
