import csv
import sys
# report.py
#
# Exercise 2.4

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

def read_portfolio(filename: str) -> list:
    portfolio = []
    with open(filename,"r") as f:
        rows = csv.reader(f)
        headers = next(rows)
        types = [str, int, float]
        for i, row in enumerate(rows, start=1):
            try:
                holding = [func(val) for func, val in zip(types, row)]
                portfolio.append(holding)
            except ValueError:
                print(f"Row {i}: Couldn't convert {row}")
    return portfolio

def read_prices(filename: str) -> dict:
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

def make_report(portfolio, prices) -> list:
    report = []
    for holding in portfolio:
        d = {}
        name, shares, price = holding
        change = prices[name] - price
        d["name"] = name
        d["shares"] = shares
        d["price"] = price
        d["change"] = change
        report.append(d)
    return report

def calc_current_price(report, prices):
    return sum(s['shares'] * prices[s['name']] for s in report)

def calc_portfolio_cost(report):
    return sum(s['shares'] * s['price'] for s in report)

def print_report(pcost, currentp, report):
    print(f"Portfolio cost is {pcost}\nCurrent value is {currentp}")
    headers = ("Name", "Shares", "Price", "Change")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    separator = "----------"
    print(f"{separator:10s} {separator:10s} {separator:10s} {separator:10s}")
    for s in report:
        name = s['name']
        shares = s['shares']
        price = '$' + str(s['price'])
        change = s['change']
        print(f"{name:>10s} {shares:>10d} ${price:>10s} {change:>10.2f}")

def portfolio_report(filename1, filename2):
    portfolio = read_portfolio(filename1)
    prices = read_prices(filename2)

    report = make_report(portfolio, prices)
    current_price = calc_current_price(report, prices)
    portfolio_cost = calc_portfolio_cost(report)

    print_report(portfolio_cost, current_price, report)
