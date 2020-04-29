# 3以内的数字累加和  3 + 2 + 1 = 6
def sum_nub(num):
    if num == 1:
        return 1  # 出口 防止陷入类似的死循环
    return num + sum_nub(num - 1)   # 自己调用自己    如果不是1 重复执行累加并返回结果

age = sum_nub(3)
print(age)

# 函数内部自己调用自己

# 必须要有出口
