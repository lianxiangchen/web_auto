a=[1,2,1,2,2,2,3,4,5,6,56,7,1,3,4]

print(set(a))  # {1, 2, 3, 4, 5, 6, 7, 56}
print(a.count(1))
print(sorted(set(a), key=lambda x:a.count(x), reverse=True))


b = [(i, a.count(i)) for i in set(a)]
print(b)
b.sort(key=lambda x:x[1], reverse=True)
print(b)

print(list(map(lambda x:x[0], b)))

