def sum_nub(num):
    #if num == 1:   # 注释掉出口
        #return 1
    return num + sum_nub(num - 1)

age = sum_nub(3)
print(age)

# 递归没有出口 就会报错
# [Previous line repeated 996 more times]
# 超出最大递归深度
#　不同的计算机最大递归深度可能不一样