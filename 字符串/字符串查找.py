# .find()
# .index()
# .rfind()
# .count()
mysql = 'Use other peoples hearts to play mahjong to opposite wanda'
print(mysql.find('to',5,30))
print(mysql.find('tos'))     # 查找不存在  显示-1


print(mysql.index('to'))   #index查找不存在 就会报错    存在就返回下标

print(mysql.count('to'))   # 查证出现次数 没有就显示为0