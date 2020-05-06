# 应用案例
# 批量修改文件名 既可添加指定字符 也可以删除指定字符

import os
# 1.找到所有文件
# 构建条件

flag = 2

file_list = os.listdir()
print(file_list)
# 2.构建文件名　
for i in file_list:
    if flag == 1:
        new_name = 'python_' + i    # 新名字的拼接

# 删除python_   构建条件 创建if语句
    elif flag == 2:
        num = len('python_')
        new_name = i[num:]
    os.rename(i, new_name)     # 重命名








