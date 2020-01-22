# The difference between a, and a[:]
a = [2, 3, 5]
print(id(a))
a[:] = [2, 3, 5]
print(id(a))

# unzip a list
a = [(1, 2), (3, 4), (5, 6)]
print(list(zip(*a)))