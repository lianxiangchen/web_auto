"""
有一个纯数字组成的字符串, 返回连续单一数字子串的个数
输入字符串： “22252”
只含单一数字的子串是
1个字符：2出现4次，5出现1次
2个字符  22 出现2 次
3个字符  222 出现1 次
4个子串 0次
5个字符 0次
总共 4+1+2+1 =8
输出结果：8
 
示例:
输入：22252
输出： 8
"""


# a = '22252'
a = input("输入：")
s = 0
for i in range(1, len(a)+1):
    b = []
    for j in range(len(a)):
        # print(a[j:j+i])
        new_a = a[j:j+i]
        # 判断是不是单一的
        if new_a.count(new_a[0]) == i:
            b.append(new_a)
    print(b)
    s += len(b)
print("输出：", s)

