student = [
    {'name':'tom','age':20},
    {'name':'rose','age':19},
    {'name':'jack','age':22},
]


# sort(key = lambda...., revers= bool数据（布尔形数据）)    sort可以对列表进行排序  revers默认值为false为升序 为true是降序
# name key 升序排列
student.sort(key=lambda x: x['name'])


print(student)  # 首字母升序排序
student.sort(key=lambda x: x['name'],reverse=True)
print(student) # 首字母降序排序


# age值升序排序
student.sort(key=lambda x: x['age'])   # 形参 x 自定义
print(student)