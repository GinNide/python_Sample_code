# 在python中 值是靠引用来传递的
# a = 1
# b = a
# print(id(a))   # id() 判断id值  在内存的内存地址
# print(id(b))   # 值是一样的
#
# a = 2
# print(id(a))
# print(id(b))
#

# 列表
aa = [10,20]
bb =  aa
print(id(aa))
print(id(bb))   # 内存地址一致
aa.append(52)
print(aa)
print(bb)
print(id(aa))
print(id(bb))