import yfinance as yf
import plotly.graph_objects as go

# Download historical stock data for Apple (AAPL)
stock_data = yf.download('AAPL', start='2020-01-01', end='2024-08-01')

# Plotting the candlestick chart with Plotly
fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                     open=stock_data['Open'],
                                     high=stock_data['High'],
                                     low=stock_data['Low'],
                                     close=stock_data['Close'])])
fig.update_layout(title='AAPL Candlestick Chart', xaxis_title='Date', yaxis_title='Price')

# Display the figure
fig.show()