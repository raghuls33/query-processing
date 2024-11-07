import pandas as pd
import numpy as np

# Create a dataframe with 10 rows and 4 columns of random values
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Define a function to apply the conditional formatting
def highlight_negatives(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Apply the function with the updated method (Styler.map)
df_styled = df.style.map(highlight_negatives)

# Display the styled dataframe
print(df_styled)