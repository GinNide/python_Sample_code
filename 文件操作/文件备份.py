# 文件备份
# 接收用户输入的文件名
# 备份文件写入数据


old_name = input('输入你要备份的文件名：')
print(old_name)

# 获取后缀 找到名字中的点 然后分离名字和后缀 最右侧的点才是后缀的点  字符串中查找某个串 用rfind
index = old_name.rfind('.')
# print(index)

# 切片找原名字
# print(old_name[:index])   提取名字　index为下标地址
# print(old_name[index:])   提取后缀名
new_name = old_name[:index] + '[备份]' + old_name[index:]
# print(new_name)


# 备份文件写入数据（数据和原文件一致）
# 打开源文件和备份文件
old_f = open(old_name,'rb')   # 以二进制 只读打开
new_f = open(new_name,'wb')   # 以二进制 写入打开
# 如果不确定文件大小 那就循环读取写入 当读取出来的文件没有了就终止循环
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break

    new_f.write(con)

old_f.close()
new_f.close()

