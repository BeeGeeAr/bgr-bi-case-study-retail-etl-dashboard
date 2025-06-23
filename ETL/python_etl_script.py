
import pandas as pd
import os

# Define paths
data_folder = os.path.join(os.getcwd(), 'Data')
output_folder = os.path.join(os.getcwd(), 'ETL')
input_file = os.path.join(data_folder, 'sales_data_mock.csv')
output_file = os.path.join(output_folder, 'sales_data_cleaned.csv')

# Load raw sales data
df = pd.read_csv(input_file)

# Convert OrderDate to datetime format
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

# Round UnitPrice to 2 decimals
df['UnitPrice'] = df['UnitPrice'].round(2)

# Standardize Status field
status_map = {
    'Completed': 'Closed',
    'Pending': 'Open',
    'Cancelled': 'Void'
}
df['OrderStatus'] = df['Status'].map(status_map)

# Drop original Status column
df.drop(columns=['Status'], inplace=True)

# Recalculate TotalAmount
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Output cleaned data
df.to_csv(output_file, index=False)

print("ETL complete. Cleaned data saved to:", output_file)
