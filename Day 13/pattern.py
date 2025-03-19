# n = int(input('Enter number: '))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(end='  ')
#     for k in range(i):
#         print('*',end=' ')
#     print()


# n = int(input('Enter number: '))
# for i in range(n , 0,-1):
#     for j in range(n-i):
#         print(end='  ')
#     for k in range(i):
#         print('*',end=' ')
#     print()

# n = int(input('Enter number: '))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()


# n = int(input('Enter number: '))

# for i in range(n):
#         for j in range(n-i):
#             print(end='  ')
#         for k in range(i*2-1):
#             print('*',end=' ')
#         print()

n = int(input('Enter input: '))

for i in range(n):
    for j in range(n):
        if i == j:
            print('1', end=' ')
        else:
            print('0' , end=' ')
    print()

