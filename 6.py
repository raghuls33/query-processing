import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Date': pd.to_datetime([
        '2020-04-01', '2020-04-02', '2020-04-03', '2020-04-06', 
        '2020-04-07', '2020-04-08', '2020-04-09', '2020-04-13',
        '2020-04-14', '2020-04-15'
    ]),
    'Close': [1105.62, 1108.84, 1097.58, 1186.92, 1188.51, 1210.26, 1211.45, 1217.56, 1262.47, 1262.47],
    'Volume': [2343100, 2936900, 2314300, 2664700, 2961800, 1971500, 2175400, 1793000, 1571200, 2971700]
}
df = pd.DataFrame(data)
start_date = '2020-04-01'
end_date = '2020-04-15'
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['Volume'], filtered_df['Close'], color='blue', alpha=0.5)
plt.title("Alphabet Inc. Trading Volume vs Stock Prices")
plt.xlabel("Volume")
plt.ylabel("Stock Price (Close)")
plt.grid(True)
plt.show()