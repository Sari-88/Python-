import yfinance as yf
import pandas as pd

# Download GameStop (GME) stock data
gme_data = yf.download("GME", start="2020-01-01", end="2023-01-01")

# Reset the index
gme_data_reset = gme_data.reset_index()

# Display the first five rows
print(gme_data_reset.head())

# Optionally, save the DataFrame to a CSV file
gme_data_reset.to_csv('gme_stock_data.csv', index=False)
