import pandas as pd

# Load the scraped data
df = pd.read_csv('Election Commission of India.csv')

# Display the initial structure of the dataframe
print("Initial DataFrame:")
print(df.head())

# Identify and drop duplicate rows if any
df = df.drop_duplicates()

# Remove unnecessary whitespaces and line breaks
df.columns = df.columns.str.strip().str.replace('\n', '')

# Drop any rows with all NaN values (if applicable)
df = df.dropna(how='all')

# Display the cleaned structure of the dataframe
print("\nCleaned DataFrame:")
print(df.head())

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)
