# build in function
color = ("red", "green", "blue", "white", "red", 59, 90, 23)
print(color)
print(len(color))
# print(min(color)) # error
x = (89, 78, 78, 75, 44)
print(min(x))
print(max(x))
print(sum(x))
# print(sorted(color)) # error
print(sorted(x))

# Operators
color = color + x
print(color, id(color))
print(x * 3)

z = 'red'

# Method
print(color.count('red'))
print(color.index('red'))

# Delete tuple object
del z
# print(z) # error

