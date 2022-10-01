A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))

# zip()   [('a', 1), ('b', 2), ('c', 3),('d', 4),('e', 5)]
# A0 {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

A1 = range(10)  # 返回值是 range(0, 10) object
# A1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

A2 = [i for i in A1 if i in A0]
# A2 = []
A3 = [A0[s] for s in A0]   # A0 等价于 ['a', 'b', 'c', 'd', 'e]
# A3 = [1, 2, 3, 4, 5]

A4 = [i for i in A1 if i in A3]
# A4 = [1, 2, 3, 4, 5]

A5 = {i:i*i for i in A1}
# A5 = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:26, 7:49, 8:64, 9:81}

A6 = [[i,i*i] for i in A1]
# [[0,0], [1,1], [2,4], [3,9], [4,16], [5,25], [6,26], [7,49], [8,64], [9,81]]

print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)






