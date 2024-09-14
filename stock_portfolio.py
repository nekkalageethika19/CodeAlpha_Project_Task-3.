import yfinance as yf  # type: ignore
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Ticker', 'jhon', 'Purchase Price'])
        
    def add_stock(self, ticker, jhon, purchase_price):
        # Check if the stock is already in the portfolio
        if ticker in self.portfolio['Ticker'].values:
            print(f"{ticker} is already in the portfolio.")
            return
        # Add new stock to the portfolio
        new_stock = pd.DataFrame([[ticker, jhon, purchase_price]], columns=['Ticker', 'jhon', 'Purchase Price'])
        self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)
        print(f"Added {ticker} to the portfolio.")
    
    def remove_stock(self, ticker):
          # Remove stock from the portfolio
        self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]
        print(f"Removed {ticker} from the portfolio.")
    
    def get_stock_data(self, ticker):
         # Fetch real-time stock data
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')
        if data.empty:
            return None
        return data['Close'].iloc[0]
    
    def track_performance(self):
         # Calculate the current value of the portfolio
        self.portfolio['Current Price'] = self.portfolio['Ticker'].apply(self.get_stock_data)
        self.portfolio['Value'] = self.portfolio['jhon'] * self.portfolio['Current Price']
        self.portfolio['Profit/Loss'] = (self.portfolio['Current Price'] - self.portfolio['Purchase Price']) * self.portfolio['jhon']
        
         # Display portfolio performance
        print(self.portfolio)
        total_value = self.portfolio['Value'].sum()
        total_profit_loss = self.portfolio['Profit/Loss'].sum()
        print(f"Total Portfolio Value: ${total_value:.2f}")
        print(f"Total Profit/Loss: ${total_profit_loss:.2f}")

           # Example usage:
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10, 150)  # Apple stock
portfolio.add_stock('GOOGL', 5, 1000) # Google stock
portfolio.track_performance()
portfolio.remove_stock('AAPL')
portfolio.track_performance()