import csv
import sys
# report.py
#
# Exercise 2.4

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

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

def read_prices(filename):
    stock_prices = {}
    with open(filename,"r") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except IndexError:
                #print("Empty list index")
                continue
    return stock_prices

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

def make_report():
    report = []
    for holding in portfolio:
        name, shares, price = holding
        change = prices[name] - price
        d = (name, shares, price, change)
        report.append(d)
    return report

current_price = 0
portfolio_cost = 0
for name, shares, cost in portfolio:
    current_price += prices[name] * shares
    portfolio_cost += shares * cost

print(f"Portfolio cost is {portfolio_cost}\nCurrent value is {current_price}")
report = make_report()
print(report)
headers = ("Name", "Shares", "Price", "Change")
print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
separator = "----------"
print(f"{separator:10s} {separator:10s} {separator:10s} {separator:10s}")
for name, shares, price, change in report:
    price = "$" + str(price)
    print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")
