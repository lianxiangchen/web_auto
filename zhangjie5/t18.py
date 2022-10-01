import os
# path = r'D:\MyDjango'
# print(os.listdir(path))
#
# # 判断是否是一个文件
# for file_name in os.listdir(path):
#     # print(file_name)
#     # 拼接路径
#     child = os.path.join(path, file_name)
#     # print(child)
#     # 判断哪些是文件，哪些是文件夹
#     if os.path.isfile(child):
#         print("文件：", child)
#     else:
#         print("文件夹：", child)

def print_directory_contents(sPath):
    for file_name in os.listdir(sPath):
        # print(file_name)
        # 拼接路径
        child = os.path.join(sPath, file_name)
        # print(child)
        # 判断哪些是文件，哪些是文件夹
        if os.path.isfile(child):
            print("文件：", child)
        else:
            print("文件夹：", child)
            # 递归函数
            print_directory_contents(child)

if __name__ == '__main__':
    sPath = r'D:\MyDjango'
    print_directory_contents(sPath)