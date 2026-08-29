from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Start Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open cryptocurrency website
driver.get("https://coinmarketcap.com/")
time.sleep(5)

# Find cryptocurrency rows
rows = driver.find_elements(By.XPATH, "//table//tbody/tr")

data = []

# Collect first 10 cryptocurrencies
for row in rows[:10]:
    try:
        cells = row.find_elements(By.TAG_NAME, "td")

        if len(cells) >= 4:
            name = cells[2].text
            price = cells[3].text

            data.append({
                "Cryptocurrency": name,
                "Price": price
            })

    except Exception:
        continue

# Close browser
driver.quit()

# Create DataFrame
df = pd.DataFrame(data)

# Display output
print("\nCryptocurrency Price Tracker")
print("============================")
print(df)
df['Cryptocurrency'] = df['Cryptocurrency'].astype(str).str.replace(r'Buy$', '', regex=True).str.strip()

def split_crypto(text):
    half_len = len(text) // 2
    if len(text) >= 4 and text[:half_len] == text[half_len:]:
        return text[:half_len], text[half_len:]
    import re
    match = re.search(r'([A-Z]{3,4})$', text)
    if match:
        symbol = match.group(1)
        name = text[:-len(symbol)]
        return name, symbol
    return text, ""
from datetime import datetime

# Get current time for Timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a new DataFrame with all requested fields
df = pd.DataFrame({
    'Rank': rank_list,              # List containing rank data
    'Coin': crypto_names_list,      # List containing crypto names
    'Price': price_list,            # List containing prices
    '24h Change': change_24h_list,  # List containing 24h change percentage
    'Market Cap': marketcap_list,   # List containing market cap values
    'Timestamp': current_time       # Same timestamp assigned to all rows
})

# Clean and convert Price column to numeric format
df['Price'] = df['Price'].astype(str).str.replace(r'[\$,]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Clean and convert Market Cap column to numeric format
df['Market Cap'] = df['Market Cap'].astype(str).str.replace(r'[\$,]', '', regex=True)
df['Market Cap'] = pd.to_numeric(df['Market Cap'], errors='coerce')

# Arrange and select columns in the exact order for Excel output
df = df[['Rank', 'Coin', 'Price', '24h Change', 'Market Cap', 'Timestamp']]

# Save the final data to CSV and Excel files
df.to_csv("crypto_prices.csv", index=False)
df.to_excel("crypto_prices.xlsx", index=False)

print("\nData saved successfully!")
print("Excel file: crypto_prices.xlsx")
print("CSV file: crypto_prices.csv")
# Save as Excel
df.to_excel("crypto_prices.xlsx", index=False)

# Save as CSV
df.to_csv("crypto_prices.csv", index=False)

print("\nData saved successfully!")
print("Excel file: crypto_prices.xlsx")
print("CSV file: crypto_prices.csv")