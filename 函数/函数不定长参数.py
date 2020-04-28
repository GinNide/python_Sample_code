# 不定长参数  也叫可变参数    不确定参数个数 可以包裹关键字和包裹位置参数
def age_info(*args):        # 包裹位置传递   最好用 *args 做包裹位置传递
    print(args)

age_info('list1')              # 返回一个元组
age_info('list1',15455,{'dad','ada'})    # 想怎么传就怎么传



