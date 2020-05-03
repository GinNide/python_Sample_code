# read()
# 文件对象.read(num)   num表示从文件中读取的数据长度（字节是单位）如果没有这个参数就是读取全部数据


# f = open('test.txt','r')

# print(f.read(10))   # 输入的是10 但是实际打印出来是9个  因为换行了  因为换行符 /n 占用一个字节数

# f.close()


# readines()
# readines可以按照行的方式把整个文件中的内容进行一次性读取，并返回一个列表，其中每一行的数据为一个元素
# f = open('test.txt','r')
# lst = f.readlines()
# print(lst)    # 会打印换行符，返回一个列表
# f.close()     # 关闭文件


# readline()       # 以 行 为单位打印  调用多次读多行
f = open('test.txt','r')
lst = f.readline()
print(lst)


lst = f.readline()
print(lst)
f.close()