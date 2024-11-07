import pandas as pd
import matplotlib.pyplot as plt

# Load Alphabet Inc. stock data
df = pd.read_csv('alphabet_stock.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Specify the start and end dates
start_date = '2023-01-01'
end_date = '2023-12-31'

# Filter data for the specified date range
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Plotting the closing stock prices
plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Date'], filtered_df['Close'], label='Close Price', color='b')
plt.title("Alphabet Inc. Historical Stock Prices")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.legend()
plt.grid(True)
plt.show()
