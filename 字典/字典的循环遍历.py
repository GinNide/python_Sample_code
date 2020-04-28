t1 = {'name':'tom','age':'58','gender':'男'}
# for k in t1.keys():           # key的遍历
#     print(k)
# print('...........')
# for v in t1.values():         # values的遍历
#     print(v)
# print('...........')
# for t in t1.items():          # 键值的遍历
#     print(t)
             
for key, value in t1.items():            # items 返回的是一个个元组,元组存有两个数据 对元组的分离  所以可以用两个变量
    print(f'{key} = {value}')            # f 去格式化输出 key 和 value
