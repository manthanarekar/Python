# Lambda Function : Anonymous function (not known function) without


# with def
# def show():
#     print("Def function")
# show()

# with lambda
# show = lambda: print("Lambda Function")
# show()

# Lambda with argument
# Type 1
addition = lambda a, b: print("Addition : ", a + b)
addition(2, 3)

# Type 2
(lambda a, b: print("Substraction : ", a - b))(2, 3)

# Lambda with if / else
# WAp to check number is positive or negative by using lambda
(lambda a: print(a, "+ve number") if a > 0 else print(a, "-ve number"))(-4)
(lambda a: print(a, "+ve number") if a > 0 else print(a, "-ve number"))(4)


