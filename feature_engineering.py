import pandas as pd

# Load your cleaned dataset
df = pd.read_csv("uber_cleaned.csv")

# Convert pickup_datetime to datetime
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

# Create new time-based features
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['weekday'] = df['pickup_datetime'].dt.day_name()

# Create peak/off-peak time indicator
def peak_hour(hour):
    return 1 if (7 <= hour <= 9 or 17 <= hour <= 19) else 0

df['is_peak_hour'] = df['hour'].apply(peak_hour)

# Encode weekday (One-Hot Encoding)
weekday_dummies = pd.get_dummies(df['weekday'], prefix='weekday')

# Combine encoded columns with original data
df = pd.concat([df, weekday_dummies], axis=1)

# Preview new features
print(df[['pickup_datetime', 'hour', 'day', 'month', 'weekday', 'is_peak_hour'] + list(weekday_dummies.columns)].head())

# Save enhanced dataset
df.to_csv("uber_enhanced.csv", index=False)
print("\n✅ Feature engineering complete! Saved as 'uber_enhanced.csv'")
