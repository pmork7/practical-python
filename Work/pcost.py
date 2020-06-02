# pcost.py
#
# Exercise 1.27
total_cost = 0
with open("Data\portfolio.csv","r") as f:
    next(f)
    for line in f:
        line = line.replace("\n","")
        items = line.split(",")
        total_cost += float(items[1]) * float(items[2])
print(f"Total cost is ${total_cost}")
