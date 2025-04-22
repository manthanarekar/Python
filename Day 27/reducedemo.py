import functools as func


def sum(x, y):
    return x + y


print(func.reduce(sum, range(1, 11)))


def sumofdigit(n):
    n = int(n)
    print(n, type(n))
    sum = 0
    while n > 0:
        rem = n % 10
        n = n // 10
        sum += rem
    return int(sum)


print(func.reduce(sumofdigit, ["123"]))
print(list(map(sumofdigit, [123, 12])))
