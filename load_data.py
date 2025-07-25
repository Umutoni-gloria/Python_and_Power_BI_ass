import pandas as pd 

# Load the dataset
df = pd.read_csv("uber.csv")

# Show first few rows
print(df.head())

# Show structure and data types
print("\n--- DataFrame Info ---")
print(df.info())

# Show any missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())
