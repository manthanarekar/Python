# copy()
x = {1, 3}
y = {4, 5}
print(x, id(x))
print(y, id(y))

z = x.copy()  # Same data with different ID
print(z, id(z))

m = x  # Same data and Same ID
print(m, id(m))

y = x.copy()
print(y, id(y))

print(m == x)  # True
print(m is x)  # True
print(z == x)  # True
print(z is x)  # False

# pop() | remove() | discard()
x.update({6, 7, 8, 11, 20, 10})
# print(x)
# x.pop()
# print(x)

# remove() #Speified elemet
x.remove()

# discard()
x.discard(100)

# clear()
x.clear()

# del
del x

# forzenset
colors = {"red"}
print(colors, type(colors), id(colors))
colors.add("green")
print(colors, type(colors), id(colors))
colors = frozenset(colors)
# After frozen you will not able to add any element in set


