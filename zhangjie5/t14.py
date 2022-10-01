from copy import deepcopy, copy

# 不可变对象 int  str  tuple
# 可变对象 list set dict

li = [1, 2, [3, 4]]

li2 = li
li_sliced = li[:]   # 切片
li_copied = copy(li)   # 浅拷贝
li_deep_copied = deepcopy(li)   # 深拷贝

li[0] = 888      # 不可变
li[2][0] = 666   # 可变
print(li_sliced, li_copied, li_deep_copied)
print(li)
print(li2)
# li_sliced [1, 2, [666, 4]]
# li_copied [1, 2, [666, 4]]
# li_deep_copied [1, 2, [3, 4]]