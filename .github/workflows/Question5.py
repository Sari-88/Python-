import yfinance as yf
import matplotlib.pyplot as plt

# Download Tesla stock data
tesla_data = yf.download("TSLA", start="2020-01-01", end="2023-01-01")

# Define the function to create a graph
def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Adj Close'], label="Tesla Stock Price")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Adjusted Closing Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot Tesla Stock Data with title
make_graph(tesla_data, "Tesla Stock Price (2020-2023)")
