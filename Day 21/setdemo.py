# s = {}  # defalut dict
# s = set()  # empty set

# s = {23, "Hello", 4.5, 6j, True, None, 23, 6j}
# s = {(1, 2, 3), (1, 2, 3), (1, 2, 3), 1, 2, 3}
# print(len(s))
# print(s)

# # Operataors
# a = {1, 2, 3}
# b = {3, 4, "Java"}
# c = {5, 6, 7, 8}
# d = {1, 2, 3, 8, 9}

# # print(a + b)
# print(a - b)
# print(a < d)
# # print(a * c)

# print(a in d)
# print(d in a)

x = {1,2,3,4}
y = {2,4,5,6}
print('x : ', x)
print('y : ', y)

print(x.union(y))
print(y.union(x))
print(x.intersection(y))
print(y.intersection(x))
print(x.difference(y))
print(y.difference(x))
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))