# 如果键 存在 就返回值 
# 如果键 不存在 就会报错

t1 = {'name':'tom','age':'58','gender':'男'}

# print(t1['name'])  # 存在就会返回值  不存在就会报错



# get()
# print(t1.get('name'))
# print(t1.get('sad','asdasd'))   # 不存在就显示 后面的值 
# print(t1.get('sad'))            #  后面的 值没有 就显示 none 




# keys()   查找字典中所有的键 返回可迭代的对象 
print(t1.keys())



# values   查找字典中所有的值  返回可迭代的对象 
print(t1.values())


# items   查找 字典中的所有键值 并返回可迭代对象  并以元组形式表示出来　
print(t1.items())

# 后面三个很重要