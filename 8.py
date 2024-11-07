import pandas as pd
data = {
    'Item': ['Item_A', 'Item_B', 'Item_A', 'Item_C', 'Item_B', 'Item_A'],
    'UnitsSold': [10, 5, 15, 20, 10, 8]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, 
                             index='Item', 
                             values='UnitsSold', 
                             aggfunc='sum')
print(pivot_table)