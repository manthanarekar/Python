# Comprehension is replacement of traditional loop and alse generate result in sequence
# # Syntax
# # [expression(output) for i(itrable_variable) if condition]
# print([i for i in range(1,6)])

# #WAp to show all even number from 1 to 10
# print([i for i in range(2,11,2)])
# print([i for i in range(1,11) if i % 2 == 0])

# WAp to show squence of 1 to 10
[print(i**2) for i in range(1, 11)]

str = input("Enter string : ")
[print(i, end="") for i in str if i.lower() not in "a,e,i,o,u"]
