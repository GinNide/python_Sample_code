# lst1 = []
# for i in range(1,3):
#    for j in range(3):
#        list1.append((i,j))
# rint(list1)
# 


list2 = [ (i,j) for i in range(1,3) for j in range(3) ]  # 因为返回的是元组  所以 i， j 要用 （）起来
print(list2)