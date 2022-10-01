import re

while True:
    a = input("请输入邮箱：")
    if a == "q" or a == "Q":
        quit()

    if re.match('^[0-9a-zA-Z_]{1,18}@[0-9a-zA-Z]{1,15}\.com$', a):
        username = re.findall('^(.+?)@', a)
        print("用户名：", username[0])
        companyname = re.findall('@(.+?)\.com', a)
        print("公司名称：", companyname[0])
    else:
        print("incorrect email format")