#  replace() 替换
message = 'Use other to  people\'s hearts to play mahjong to opposite wanda'
# age = message.replace('to','kkkk')    # 可以改变替换次数  替换次数 大于 出现次数 意味着所以出现全部被替换
# print(age)

# 元数据并没有被修改 只是修改了replace的返回值
# 说明了 字符中不可以改变数据类型
# 数据分为可变换类型 和 不可变类型 


# split()  分割
list1 = message.split('to')
print(list1)
# 输出会丢失分割字符

#  join()
mylist = ['aa','bb','cc']
new = '...'.join(mylist)
print(new)


# capitalize() 将字符串的首字母大写 
# .title() 每个单词首字母都大写
# upper() 把字符串中的小写转大写
# lower() 把 字符串中的大写换小写