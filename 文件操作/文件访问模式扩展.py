'''
测试目标
1. r+ w+ a+
2. 文件指针对数据读取的影响
'''

# r+
# f = open('test.txt','r+')    区别 r 没有文件则报错 可以正常读取数据 因为文件指针在最前面
#
# message = f.read()
# print(message)
# f.close()


# w+                           区别 w 没有文件就会新建一个 特点 文件指针在开头 用新内容迁移覆盖原内容
# f = open('test.txt','w+')
# messgae = f.read()     # 读取不到数据 因为被覆盖了 而且后续没有写入数据所以是空的
# print(messgae)


# a+                           区别 a 没有文件也新建一个  特点 文件指针在结尾，无法读取数据 在结尾追加数据
f = open('test.txt', 'a+')
message = f.read()  # 文件指针在结尾　结尾后面没有数据所以读取不到
print(message)
