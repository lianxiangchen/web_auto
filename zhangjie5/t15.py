from functools import reduce

# 1-100的和
print(reduce(lambda x,y:x+y, range(1, 101)))

print(list(map(lambda x:x*x, range(1, 11))))

print(list(filter(lambda x: "c" in x, ["a", "ab", "abc", "bc", "cd"] )))