a = [
    {"yoyo1": "123456"},
    {"yoyo2": "123456"},
    {"yoyo3": "123456"},
]

with open("xx.txt", "a", encoding="utf-8") as fp:
    for i in a:
        # print(i)
        for j in i.items():
            # print(j[0]+','+j[1])
            fp.write(j[0]+','+j[1]+"\n")