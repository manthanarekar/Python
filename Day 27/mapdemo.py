# map() -> produce result in sequence but take function and list of input

# Syntax : map(function,listofinput)


# without lambda find square of 1 to 10 number
def square(x):
    return x**2


print(list(map(square, range(1, 11))))
print(tuple(map(square, (1, 2, 3))))

# with lambda find square
print(list(map(lambda x: x**2, range(1, 11))))


# Addition of two
def addition(x, y):
    return x + y


print(list(map(addition, (4, 5), (5, 6))))
print(list(map(addition, range(5, 10), range(1, 6))))
print(list(map(addition, (4, 5), (5, 6))))
print(list(map(addition, (4, 5), (5, 6))))


# example - 3
animals = ["cat", "dog", "tiger"]
print(list(map(set, animals)))








