# seek()  用来移动文件指针
# 文件对象.seek(偏移量,起始位置)
# 0 文件开头
# 1 当前结尾
# 2 文件结尾


#　f = open('test.txt','r+')
f = open('test.txt','a+')
# f.seek(0,2)   # r+ 改变读取数据开始位置

f.seek(0,0)   # a+ 改变读取数据开始位置         偏移量不写默认为0

con = f.read()
print(con)
f.close()