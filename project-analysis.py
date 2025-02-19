import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportion_confint
import numpy as np

# Read the CSV file
data = pd.read_csv('project-data.csv')

# Create gender distribution charts
gender_counts = data['Please select your gender'].value_counts()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Bar chart
gender_counts.plot(kind='bar', ax=ax1)
ax1.set_title('Gender Distribution (Counts)')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Number of Respondents')
ax1.tick_params(axis='x', rotation=0)
for i, count in enumerate(gender_counts):
    ax1.text(i, count + 0.1, str(count), ha='center', va='bottom')

# Pie chart
total = gender_counts.sum()
percentages = gender_counts / total * 100
gender_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_title('Gender Distribution (Percentages)')

plt.tight_layout()
plt.savefig('gender_distribution.png')
print("----------------------------------------")
print("Gender Distribution Analysis:")
print(gender_counts)
print("----------------------------------------\n")
print("\n")
# Spicy Food Preference Analysis

# Create spicy food preference charts
spicy_food_counts = data['Do you like spicy food? (please choose one)'].value_counts()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Bar chart
spicy_food_counts.plot(kind='bar', ax=ax1)
ax1.set_title('Spicy Food Preference (Counts)')
ax1.set_xlabel('Likes Spicy Food?')
ax1.set_ylabel('Number of Respondents')
ax1.tick_params(axis='x', rotation=0)
for i, count in enumerate(spicy_food_counts):
    ax1.text(i, count + 0.1, str(count), ha='center', va='bottom')

# Pie chart
total = spicy_food_counts.sum()
percentages = spicy_food_counts / total * 100
spicy_food_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_title('Spicy Food Preference (Percentages)')

plt.tight_layout()
plt.savefig('spicy_food_preference.png')
print("----------------------------------------")
print("Spicy Food Preference Analysis:")
print(spicy_food_counts)
print("----------------------------------------\n")

# Calculate and print confidence interval for spicy food preference (proportion of 'Yes')
n_spicy_yes = spicy_food_counts['Yes']
n_spicy_total = len(data)
conf_interval_spicy = proportion_confint(n_spicy_yes, n_spicy_total, method='wilson')
print(f"Confidence Interval for Spicy Food Preference (Yes Proportion): {conf_interval_spicy}")
print("\n")

# Pineapple on Pizza Preference Analysis
# Create pineapple on pizza preference charts
pineapple_pizza_counts = data['Do you like pineapples on your pizza (please choose one)'].value_counts()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Bar chart
pineapple_pizza_counts.plot(kind='bar', ax=ax1)
ax1.set_title('Pineapple on Pizza Preference (Counts)')
ax1.set_xlabel('Likes Pineapple on Pizza?')
ax1.set_ylabel('Number of Respondents')
ax1.tick_params(axis='x', rotation=0)
for i, count in enumerate(pineapple_pizza_counts):
    ax1.text(i, count + 0.1, str(count), ha='center', va='bottom')

# Pie chart
total = pineapple_pizza_counts.sum()
percentages = pineapple_pizza_counts / total * 100
pineapple_pizza_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
ax2.set_title('Pineapple on Pizza Preference (Percentages)')

plt.tight_layout()
plt.savefig('pineapple_pizza_preference.png')
print("----------------------------------------")
print("Pineapple on Pizza Preference Analysis:")
print(pineapple_pizza_counts)
print("----------------------------------------\n")

# Calculate and print confidence interval for pineapple on pizza preference (proportion of 'Yes')
n_pineapple_yes = pineapple_pizza_counts['Yes']
n_pineapple_total = len(data)
conf_interval_pineapple = proportion_confint(n_pineapple_yes, n_pineapple_total, method='wilson')
print(f"Confidence Interval for Pineapple on Pizza Preference (Yes Proportion): {conf_interval_pineapple}")
