# x = {1,2,3,4}
# y = {2,4,5,6}
# z = {1,2}
# p = {11,12}
# print('x : ', x)
# print('y : ', y)

# print(x.issuperset(z))
# print(x > z) # True
# print(y.issubset(x))
# print(x.isdisjoint(p)) # True - check insertion is null or not if null then True other wise false

# Adding element

# mylist = set()
# mylist.add('Red')
# print(mylist)
# mylist.add('Red')
# print(mylist)
# # mylist.add('Red','Green') # error only single elemet
# mylist(('green','blue'))
# print(mylist)
# x = ('green','white')
# mylist.add(x)

# WAP to take number as per count and show sum of then show voa loop
# count = int(input("Enter count of number : "))
# sum = 0
# mylist = (int(input('Enter number to sum : ')) for i in range(count))
# sum = [sum + i for i in mylist]
# print(mylist)

# Update()
colors = {"Red", "Green"}
colors.update({800})
print(colors)
x = {34, 56, 67}
x.update(colors)
print(x)
colors.update(())