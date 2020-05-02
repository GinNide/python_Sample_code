# 文件操作的基本步骤
# 打开文件
# 读写
# 关闭文件   也可以只打开和关闭文件  不进行任何读写操作


# 打开文件 open()
# open(name,mode)    name是要打开的文件名 （可以包含文件所在的路径）
#                    mode的意思是  只读，只写，追加，等 模式


f = open('test.txt','w')   # w是写的意思

# 读写 write() read()
f.write('aaaa')  # 写入aaaa

# 关闭文件
f.close()   # 关闭文件 避免消耗内存