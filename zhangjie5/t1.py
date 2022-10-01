"""
有1、2、3、4数字能组成多少互不相同无重复数的三位数?

分别打印这些组合
"""
s = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and i != k:
                print(i, j, k)
                s += 1
print("总数：", s)


from itertools import combinations, permutations

print(permutations([1, 2, 3, 4], 3))   # permutations object
for i,j,k in permutations([1, 2, 3, 4], 3):
    print(i,j,k)
print(len(list(permutations([1, 2, 3, 4], 3))))