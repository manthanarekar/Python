# Left incremental Triangle

# n = int(input('Enter number: '))
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

'''
Output

Enter number: 5
* 
* * 
* * * 
* * * * 
* * * * * 

'''

# -------------------------------------

# Left decremental Triangle

# n = int(input('Enter number: '))
# for i in range(-n+1,0):
#     for j in range(-i+1):
#         print('*',end=' ')
#     print()

'''
Output

Enter number: 5
* * * * * 
* * * * 
* * * 
* * 
* 

'''

# -------------------------------------

# count = 1
# for i in range(3):
#     for j in range(1,count+1):
#         print(j,end=' ')
#     count +=1
#     print()


# for i in range(1,4):
#     for j in range(i):
#         print(i,end=' ')
#     print()


# count = 0
# for i in range(1,4):
#     for j in range(i):
#         count +=1
#         print(count,end=' ')
#     print()

# for i in range(1,4):
#     for j in range(i+1):
#         if j == 1 :
#             print(i*1,end=' ')
#         elif j == 0:
#             pass
#         else:
#             print(i+j,end=' ')
#     print()


row = int(input('Enater number: '))

for i in range(1,row + 1):
    num = i
    for j in range(1,i+1):
        print(num, end=" ")
        num += (row - j)
    print()

'''
Output

Enater number: 5
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15 

'''