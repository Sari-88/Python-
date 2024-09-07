# Import necessary libraries
import yfinance as yf
import pandas as pd

# Download Tesla stock data from Yahoo Finance
# Ticker symbol for Tesla is 'TSLA' 
tesla_data = yf.download('TSLA', start='2020-01-01', end='2023-01-01')

# Reset the index to turn the Date from index to a column
tesla_data_reset = tesla_data.reset_index()

# Display the first five rows of the DataFrame
print(tesla_data_reset.head())
