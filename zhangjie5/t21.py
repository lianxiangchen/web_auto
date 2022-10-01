a = "ABCABADCSABBAUYIIYU"
b = []
for i in range(2, len(a)+1):
    # s = []
    for j in range(len(a)-i+1):
        new_s = a[j:j+i]
        # s.append(a[j:j+i])
        if new_s == new_s[::-1]:
            b.append(new_s)
print(b)
print("字串回文数：", len(b))


a = [2, 3, 8, 4, 9, 5, 6]
b = [2, 5, 6, 10, 17, 11]

# 集合a和b中都包含了的元素
print(set(a) & set(b))  # {2, 5, 6}

# a或b中包含的所有元素
print(set(a) | set(b)) # {2, 3, 4, 5, 6, 8, 9, 10, 11, 17}

# a中包含而集合b中不包含的元素
print(set(a) - set(b))   # {8, 9, 3, 4}

# 不同时包含于a和b的元素
print(set(a) ^ set(b))   # {3, 4, 8, 9, 10, 11, 17}
