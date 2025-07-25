import pandas as pd

# Load data
df = pd.read_csv("uber.csv")

# 1. Drop rows with missing dropoff values
df = df.dropna(subset=["dropoff_longitude", "dropoff_latitude"])

# 2. Drop the Unnamed: 0 column
df = df.drop(columns=["Unnamed: 0"])

# 3. Convert pickup_datetime to datetime
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

# 4. Remove rows with invalid fare_amount
df = df[(df['fare_amount'] > 0) & (df['fare_amount'] < 200)]  # Assume >200 is abnormal

# 5. Remove rows with invalid passenger_count
df = df[(df['passenger_count'] > 0) & (df['passenger_count'] <= 6)]

# 6. Show result
print("\n✅ Cleaned data shape:", df.shape)
print("\n✅ Any nulls remaining?\n", df.isnull().sum())


# 7. Save cleaned CSV
df.to_csv("uber_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as uber_cleaned.csv")
