a = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

print(a.split("\n"))

print([i.split(" ") for i in a.split("\n")])

print([[j for j in i.split(" ") if len(j) > 3] for i in a.split("\n")])