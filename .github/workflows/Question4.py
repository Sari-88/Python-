import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for GME revenue data
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Send a request to the website and get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the revenue table on the webpage
tables = soup.find_all("table")
for i, table in enumerate(tables):
    print(f"Table {i}: {table}")

# Parsing the correct table
# Assuming the table with revenue data is the second table (index 1)
gme_revenue_table = tables[1]

# Extract table rows and data
data = []
for row in gme_revenue_table.find_all("tr")[1:]:  # Skip header row
    columns = row.find_all("td")
    if len(columns) > 1:  # Ensure there are enough columns
        date = columns[0].text.strip()
        revenue = columns[1].text.strip().replace("$", "").replace(",", "")
        data.append([date, revenue])

# Convert to DataFrame
columns = ["Date", "Revenue"]
gme_revenue = pd.DataFrame(data, columns=columns)

# Convert 'Revenue' column to numeric type (float)
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"], errors="coerce")

# Display the last five rows of the DataFrame
print(gme_revenue.tail())
