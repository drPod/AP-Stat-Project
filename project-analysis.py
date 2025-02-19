import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportion_confint

# Read the CSV file
data = pd.read_csv('project-data.csv')

# Create gender distribution bar chart
gender_counts = data['Please select your gender'].value_counts()
plt.figure(figsize=(8, 6))
gender_counts.plot(kind='bar')
plt.title('Gender Distribution of Survey Respondents')
plt.xlabel('Gender')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=0)
for i, count in enumerate(gender_counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom') # Add count labels
plt.savefig('gender_distribution.png')
print("Gender Distribution Summary:")
print(gender_counts)
print("\n")

# Create spicy food preference bar chart
spicy_food_counts = data['Do you like spicy food? (please choose one)'].value_counts()
plt.figure(figsize=(8, 6))
spicy_food_counts.plot(kind='bar')
plt.title('Spicy Food Preference')
plt.xlabel('Likes Spicy Food?')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=0)
for i, count in enumerate(spicy_food_counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom') # Add count labels
plt.savefig('spicy_food_preference.png')
print("Spicy Food Preference Summary:")
print(spicy_food_counts)

# Calculate and print confidence interval for spicy food preference (proportion of 'Yes')
n_spicy_yes = spicy_food_counts['Yes']
n_spicy_total = len(data)
conf_interval_spicy = proportion_confint(n_spicy_yes, n_spicy_total, method='wilson')
print(f"Confidence Interval for Spicy Food Preference (Proportion of 'Yes'): {conf_interval_spicy}")
print("\n")

# Create pineapple on pizza preference bar chart
pineapple_pizza_counts = data['Do you like pineapples on your pizza (please choose one)'].value_counts()
plt.figure(figsize=(8, 6))
pineapple_pizza_counts.plot(kind='bar')
plt.title('Pineapple on Pizza Preference')
plt.xlabel('Likes Pineapple on Pizza?')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=0)
plt.savefig('pineapple_pizza_preference.png')
for i, count in enumerate(pineapple_pizza_counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom') # Add count labels
print("Pineapple on Pizza Preference Summary:")
print(pineapple_pizza_counts)

# Calculate and print confidence interval for pineapple on pizza preference (proportion of 'Yes')
n_pineapple_yes = pineapple_pizza_counts['Yes']
n_pineapple_total = len(data)
conf_interval_pineapple = proportion_confint(n_pineapple_yes, n_pineapple_total, method='wilson')
print(f"Confidence Interval for Pineapple on Pizza Preference (Proportion of 'Yes'): {conf_interval_pineapple}")
print("\n")
