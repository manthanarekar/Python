# WAP to take number from user and add into list and show even and odd number seperately
# count = int(input("Enter count of number : "))
# nums = [int(input(f'Enter {i} num : ')) for i in count ]
# even = []
# odd = []
# [ even.append(i) if i % 2 == 0 else odd.append(i) for i in nums ]

#WAP to print True for +ve number and False for -ve number but take any 10 number from user 
num = [int(input(f'Enter {i+1} number : ')) for i in range(10)]
[print(f'{i} True') if i > 0 else print(f'{i} False') for i in num ]