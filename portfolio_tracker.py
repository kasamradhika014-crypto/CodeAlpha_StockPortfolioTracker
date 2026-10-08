# Task 2: Stock Portfolio Tracker - CodeAlpha Internship
# Key Concepts: Dictionary, Input/Output, Arithmetic, File Handling

# 1. Hardcoded dictionary to define stock prices (as required by the PDF)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 175
}

# 2. Dictionary to track the user's holdings
user_portfolio = {}

print("=== Welcome to the Stock Portfolio Tracker ===")
print("Available Stocks and Current Prices:")
for stock, price in stock_prices.items():
    print(f"- {stock}: ${price}")
print("----------------------------------------------")

# 3. Input Loop: Collect stock names and quantities
while True:
    stock_input = input("\nEnter stock symbol (or type 'done' to finish): ").strip().upper()

    if stock_input == "DONE":
        break

    if stock_input not in stock_prices:
        print(f"Error: '{stock_input}' is not in the price list. Please pick from available stocks.")
        continue

    quantity_input = input(f"Enter quantity of shares for {stock_input}: ").strip()

    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print("Invalid quantity! Please enter a positive whole number.")
        continue

    quantity = int(quantity_input)

    # Accumulate quantities if entered more than once
    user_portfolio[stock_input] = user_portfolio.get(stock_input, 0) + quantity
    print(f"Added {quantity} shares of {stock_input}!")

# 4. Calculate total investment and format summary
print("\n==============================================")
print("             PORTFOLIO SUMMARY                ")
print("==============================================")

total_investment = 0
summary_lines = []

separator = "-" * 45 + "\n"
header = f"{'Stock':<10} | {'Qty':<8} | {'Price':<10} | {'Subtotal':<10}\n"

summary_lines.append("STOCK PORTFOLIO REPORT\n")
summary_lines.append(separator)
summary_lines.append(header)
summary_lines.append(separator)

print(header.strip())
print("-" * 45)

for stock, qty in user_portfolio.items():
    price = stock_prices[stock]
    subtotal = qty * price
    total_investment += subtotal

    row = f"{stock:<10} | {qty:<8} | ${price:<9} | ${subtotal:<9}\n"
    summary_lines.append(row)
    print(row.strip())

summary_lines.append(separator)
total_line = f"Total Investment Value: ${total_investment}\n"
summary_lines.append(total_line)

print("-" * 45)
print(total_line.strip())

# 5. File handling: Save output to portfolio_summary.txt (as requested in PDF)
filename = "portfolio_summary.txt"
with open(filename, "w") as file:
    file.writelines(summary_lines)

print(f"\nReport successfully saved to '{filename}'.")