# 如何判断一个字符串有没有重复字符
a = "hello"
print(True if not len(a) == len(set(a)) else False)

def isdup(a):
    for i in a:
        print(a.count(i))
        if a.count(i) > 1:
            return True
    return False

if __name__ == '__main__':
    print(isdup("hello"))
    print(isdup("world"))

