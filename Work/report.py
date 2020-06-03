# report.py
#
# Exercise 2.4
import csv
import sys
# report.py
#
# Exercise 2.4
def read_portfolio(filename):
    portfolio = []
    with open(filename,"r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", row)
    return portfolio

filename = ""
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
result = read_portfolio(filename)
print(result)
