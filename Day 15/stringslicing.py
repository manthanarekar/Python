# Slicing of string - stringname[start:end:steps]
# Rule
# Start : optional default 0
# end : optional default last char of string
# step : optinal defaulr +1

s= "welcome" #0123456

print(s)
print(s[3])
print(s[:])
print(s[::])
print(s[3:5])
print(s[3:7])
print(s[3:17])
print(s[:3])
print(s[::3])
print(s[::1])
print(s[3::3])
print(s[3:6:3])
print(s[-1:])
print(s[-4:])
print(s[:-4])

# Note
#    0   1   2   3   4   5   6 
#  | w | e | l | c | o | m | e |
#   -7  -6  -5  -4  -3  -2  -1 

# if s[::-4] it take default start -1 and 








