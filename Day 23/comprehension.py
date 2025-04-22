# dict comprehension
# syntax {expression for i in seq_object if codition }

# square of 1 to 5
# print([i*i for i in range(1,6)])
# print({i*i for i in range(1,6)})
# print({i : i*i for i in range(1,6)})


products = {"milk": 50, "coffee": 80, "bread": 28}

# WAP to convert all items price INR to US and show update item with price
print({k: v * 0.012 for k, v in products.items()})

# WAp show olny those whoes price greater then 30
print({k: v for k, v in products.items() if v > 30})

# WAP to show only coffee details
print({k: v for k, v in products.items() if k == "coffee"})
