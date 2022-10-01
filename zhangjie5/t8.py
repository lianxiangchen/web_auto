a = ['aababbc', 'badabcab']
b = []
for i in a:
    while 'ab' in i:
        i = i.replace("ab", '')
    b.append(i)
print(b)
