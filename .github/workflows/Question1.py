# Import necessary libraries
import yfinance as yf
import pandas as pd

# Download Tesla stock data from Yahoo Finance
# Ticker symbol for Tesla is 'TSLA'
try:
    tesla_data = yf.download('TSLA', start='2020-01-01', end='2023-01-01')
    
    # Check if the data was successfully downloaded
    if tesla_data.empty:
        print("No data found for the specified date range.")
    else:
        # Reset the index to turn the Date from index to a column
        tesla_data_reset = tesla_data.reset_index()
        
        # Display the first five rows of the DataFrame
        print("Tesla stock data (first 5 rows):\n", tesla_data_reset.head())
except Exception as e:
    print(f"An error occurred while fetching Tesla data: {e}")
