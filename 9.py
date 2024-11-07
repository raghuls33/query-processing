import pandas as pd
data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'North'],
    'Manager': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'],
    'Salesman': ['John', 'Mike', 'John', 'Sam', 'Mike', 'Emma'],
    'SaleAmount': [1000, 1500, 1200, 1600, 1700, 1300]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, 
                             index=['Region', 'Manager', 'Salesman'], 
                             values='SaleAmount', 
                             aggfunc='sum')
print(pivot_table)