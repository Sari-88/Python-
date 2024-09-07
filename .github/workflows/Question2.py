import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the revenue data
tables = soup.find_all('table')
# The relevant table might be the second one, so we select it
tesla_revenue_table = tables[1]

# Extract the rows from the table
rows = tesla_revenue_table.find_all('tr')

# Create a list to hold the extracted data
data = []

# Iterate over each row and extract the columns
for row in rows[1:]:  # Skip the header row
    columns = row.find_all('td')
    date = columns[0].text.strip()
    revenue = columns[1].text.strip()
    data.append([date, revenue])

# Create a DataFrame from the data
tesla_revenue = pd.DataFrame(data, columns=['Date', 'Revenue'])

# Display the last five rows of the DataFrame
print(tesla_revenue.tail())
