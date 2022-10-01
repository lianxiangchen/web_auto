a = "{[{()}]()}"

b = []
flag = True

for i in a:
    if i == "{" or i == "[" or i == "(":
        b.append(i)
    elif i == "}":
        if len(b) == 0 or b.pop() != "{":
            flag = False
    elif i == "]":
        if len(b) == 0 or b.pop() != "[":
            flag = False
    elif i == ")":
        if len(b) == 0 or b.pop() != "(":
            flag = False
if len(b) != 0:
    flag = False

print("最终结果：", flag)
