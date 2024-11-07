import pandas as pd
data = {
    'Item': ['Item_A', 'Item_B', 'Item_A', 'Item_C', 'Item_B', 'Item_A'],
    'SaleValue': [100, 200, 150, 300, 250, 120]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, 
                             index='Item', 
                             values='SaleValue', 
                             aggfunc=['max', 'min'])
print(pivot_table)
