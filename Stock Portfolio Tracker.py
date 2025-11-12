# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350
}

portfolio = {}
total_investment = 0

# User input: number of stocks to enter
num_stocks = int(input("Enter the number of different stocks: "))

for _ in range(num_stocks):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print(f"Stock {stock} not found in database. Skipping.")

# Calculate total investment
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} x {stock_prices[stock]} = {investment}")

print(f"Total Investment Value: {total_investment}")

# Saving result
save = input("Do you want to save results to a file? (yes/no): ").lower()

if save == "yes":
    file_type = input("Choose file type: txt or csv: ").lower()
    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio:")
            for stock, quantity in portfolio.items():
                f.write(f"{stock}: {quantity} x {stock_prices[stock]} = {stock_prices[stock]*quantity}")
            f.write(f"Total Investment Value: {total_investment}")
        print("Results saved to portfolio.txt")
    elif file_type == "csv":
        import csv
        with open("portfolio.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Investment"])
            for stock, quantity in portfolio.items():
                writer.writerow([stock, quantity, stock_prices[stock], stock_prices[stock]*quantity])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])
        print("Results saved to portfolio.csv")
    else:
        print("Unknown file type selected. Results not saved.")
else:
    print("Results not saved.")