# os 模块
import os  # 导入os模块
# 使用方法    os.函数名()


# 文件操作
# 文件重命名
# os.rename(目标文件名，新文件名)   目标文件名要绝对路径  同一目录不用
# os.rename('test1.txt','新建.txt')     # 重命名
# 删除文件
# os.remove()
# os.remove('新建.txt')    # 删除文件


# 　文件夹操作
#  os.mkdir('test测试')    # 创建文件夹

#  os.rmdir('test测试')    # 删除文件夹

#  print(os.getcwd())             # 返回当前文件所在目标路径

#  os.mkdir('aa')
#  需求在 aa 文件夹里面创建 bb 文件夹
os.chdir('aa')     # 切换到 aa 这个目录里
#  os.mkdir('bb')

#　获取文件夹下的所有文件名信息 返回一个列表（获取目录列表）
#  print(os.listdir())   # 打印返回信息
#  print(os.listdir('aa'))  # 返回 aa 文件夹里面的信息返回一个列表

# rename() 重命名文件夹
os.rename('bb','bbbb')   # 要先进入aa这个目录