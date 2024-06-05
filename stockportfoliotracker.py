import yfinance as yf
import pandas as pd

class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]["Quantity"] += quantity
        else:
            self.portfolio[symbol] = {"Quantity": quantity}

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]["Quantity"]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]["Quantity"] -= quantity

    def update_prices(self):
        for symbol in self.portfolio.keys():
            data = yf.Ticker(symbol).history(period="1d")
            price = data["Close"].iloc[-1]
            self.portfolio[symbol]["Price"] = price

    def portfolio_value(self):
        total_value = 0
        for symbol, data in self.portfolio.items():
            total_value += data["Quantity"] * data["Price"]
        return total_value

    def display_portfolio(self):
        print("Portfolio:")
        print("{:<10} {:<10} {:<10}".format("Symbol", "Quantity", "Price"))
        for symbol, data in self.portfolio.items():
            print("{:<10} {:<10} {:<10}".format(symbol, data["Quantity"], data["Price"]))


# Example usage
portfolio = PortfolioTracker()

# Adding stocks to the portfolio
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOG", 5)

# Displaying the initial portfolio
portfolio.display_portfolio()

# Updating prices
portfolio.update_prices()

# Displaying portfolio after updating prices
portfolio.display_portfolio()

# Calculating portfolio value
print("Portfolio Value: $", portfolio.portfolio_value())
