# String are immutable (not modifyable)
x = 'Python'
print(x,id(x))
print(x[0])
# x[0] = 'J' #Typrerror string are immutable

# But string can be modified by using method .replace()
# while doing this orignal string not getting modified i.e. string 
print(x.replace('p' , 'j'))
print(x,id(x))

x = x