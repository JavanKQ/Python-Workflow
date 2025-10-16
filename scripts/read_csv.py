import pandas as pd

# Load the CSV
df = pd.read_csv("D:/Python312/Python-Workflow/data/sales.csv")  # relative path from the scripts folder

# Show the first few rows
print(df)

# Simple calculation: total price per product
df['total'] = df['quantity'] * df['price']
print("\nWith total column:")
print(df)
