# 拆包
# 拆包元组
# def return_num():
#     return 100,200         # 会得到一个元组
# age1,age2 = return_num()
# print(age2)
# print(age1)

# 因为return 有两个数据所以 用两个变量去接收

# 字典拆包

dict1 = {'name':'tom',"age":18}
a,b = dict1    # dict1 有两个键值对 拆包用两个变量去接收
print(a)  #　得到字典的 key值
print(b)

print(dict1[a])
print(dict1[b])   # 按照 字典中的key值 去找values   (按照键去找值)
