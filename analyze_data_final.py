import pandas as pd

# Load the cleaned data
df = pd.read_csv('cleaned_data.csv')

# Display the initial structure of the dataframe
print("Cleaned DataFrame:")
print(df.head())

# Derive insights from the data
insights = []

# Example insights (adjust these based on the actual data structure and fields)
# 1. Total number of constituencies
total_constituencies = df['Title'].nunique()
insights.append(f"Total number of constituencies: {total_constituencies}")

# 2. State with the highest number of constituencies
state_constituency_counts = df['Field1'].value_counts()
top_state = state_constituency_counts.idxmax()
top_state_count = state_constituency_counts.max()
insights.append(f"State with the highest number of constituencies: {top_state} ({top_state_count})")

# 3. Average number of constituencies per state
average_constituencies_per_state = state_constituency_counts.mean()
insights.append(f"Average number of constituencies per state: {average_constituencies_per_state:.2f}")

# 4. List of states and their number of constituencies
insights.append("List of states and their number of constituencies:")
for state, count in state_constituency_counts.items():
    insights.append(f"{state}: {count}")

# Add more insights based on your data and requirements...

# Print the insights
print("\nKey Insights:")
for insight in insights:
    print(insight)

# Save the insights to a text file
with open('insights_report.txt', 'w') as f:
    for insight in insights:
        f.write(insight + '\n')
