import pandas as pd

df = pd.read_csv('Election Commission of India.csv')

print("Initial DataFrame:")
print(df.head())

df = df.drop_duplicates()

df.columns = df.columns.str.strip().str.replace('\n', '')

df = df.dropna(how='all')

print("\nCleaned DataFrame:")
print(df.head())

df.to_csv('cleaned_data.csv', index=False)
