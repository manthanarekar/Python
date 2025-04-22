# filter() -> used to check input and products single result or many sequance result

choice = ["red", "red", "blue", "green"]


def findcolor(choice):
    return choice == "red"

print(list(filter(findcolor, choice)))


