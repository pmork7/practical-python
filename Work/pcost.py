import csv
import sys
# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total_cost = 0
    with open(filename,"r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                a = row
                total_cost += float(a[1]) * float(a[2])
            except ValueError:
                print("Couldn't parse", row)
    return total_cost

filename = ""
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
cost = portfolio_cost(filename)
print(f"Total cost is ${cost}")
