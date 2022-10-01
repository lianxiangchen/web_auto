a = [11, 2, 33, 1,  5, 88, 3]
n = len(a)  # 7
print(n)
# [6,5,4,3,2,1]
for j in range(n-1, 0, -1):
    for i in range(j):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    print(a)
print(a)