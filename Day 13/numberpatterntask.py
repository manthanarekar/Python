n = int(input('Enter number: '))
count = 1
for i in range(n+1):
    for j in range(n):
        if j % 2 ==0 :
            if j%2 == 0:
                print(count,end='  ')
                count += 1
            else:
                print('*',end='  ')
        else:
            if j%2 == 0:
                print('*',end='  ')
            else:
                print(count,end='  ')
                count += 1
    print()