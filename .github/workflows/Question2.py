from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the Tesla revenue page
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
driver.get(url)

# Let the browser load fully
driver.implicitly_wait(10)  # wait for 10 seconds to let the page load completely

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the table in the page
tables = soup.find_all('table')
print(f"Number of tables found: {len(tables)}")

if len(tables) > 1:
    revenue_table = tables[1]  # The second table contains the data
    data = []
    for row in revenue_table.find_all("tr")[1:]:  # Skip the header row
        columns = row.find_all("td")
        if len(columns) > 1:
            date = columns[0].text.strip()
            revenue = columns[1].text.strip().replace("$", "").replace(",", "")
            data.append([date, revenue])
    
    # Convert to DataFrame
    revenue_df = pd.DataFrame(data, columns=["Date", "Revenue"])
    revenue_df["Revenue"] = pd.to_numeric(revenue_df["Revenue"], errors="coerce")
    
    print(revenue_df.tail())
else:
    print("Expected table not found.")

# Close the browser session
driver.quit()
