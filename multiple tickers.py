# Import packages
import yfinance as yf
import pandas as pd

# Set the start and end date
start_date = '1990-01-01'
end_date = '2024-08-1'

# Define the ticker list
tickers_list = ['AAPL', 'NVDA', 'MSFT', 'GS']

# Create placeholder for data
data = pd.DataFrame(columns=tickers_list)

# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker,
                               start_date,
                               end_date)['Adj Close']

# Print first 5 rows of the data
data.tail()
import matplotlib.pyplot as plt

data.plot(figsize=(10, 7))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('Adjusted close price of stocks')

# Show the plot
plt.show()