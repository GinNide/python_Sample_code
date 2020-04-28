t1 = ('qq','qsdf','sdfs','dsadfgg')
t2 = ('qq','qsdf','sdfs','dsadfgg',['asdsad','asdas'])
# 元组本身不能修改 但是元组里面的列表可以修改
# 最好不要修改元组  注意
t2[4][0] = 'tom'
print(t2[4][0])
print(t2)