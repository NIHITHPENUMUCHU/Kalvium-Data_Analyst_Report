import pandas as pd

df = pd.read_csv('cleaned_data.csv')

print("Cleaned DataFrame:")
print(df.head())

insights = []

total_constituencies = df['Title'].nunique()
insights.append(f"Total number of constituencies: {total_constituencies}")

state_constituency_counts = df['Field1'].value_counts()
top_state = state_constituency_counts.idxmax()
top_state_count = state_constituency_counts.max()
insights.append(f"State with the highest number of constituencies: {top_state} ({top_state_count})")

average_constituencies_per_state = state_constituency_counts.mean()
insights.append(f"Average number of constituencies per state: {average_constituencies_per_state:.2f}")

insights.append("List of states and their number of constituencies:")
for state, count in state_constituency_counts.items():
    insights.append(f"{state}: {count}")

print("\nKey Insights:")
for insight in insights:
    print(insight)

# Save the insights to a text file
with open('insights_report.txt', 'w') as f:
    for insight in insights:
        f.write(insight + '\n')
