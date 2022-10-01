a = "pwwkew"
b = []
for i in range(1, len(a)+1):
    print(i)  # 字串长度
    # s = []
    for j in range(len(a)-i+1):
        # s.append(a[j:j+i])
        if len(a[j:j+i]) == len(set(a[j:j+i])):
            b.append(a[j:j+i])
print(b)

print(max(b, key=lambda x:len(x)))
print("最长的字串个数:", len(max(b, key=lambda x:len(x))))