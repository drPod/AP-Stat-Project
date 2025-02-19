import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportion_confint
from statsmodels.stats.proportion import proportions_ztest
import numpy as np
from scipy.stats import norm

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

# Visualize confidence interval
fig_conf_int, ax_conf_int = plt.subplots(figsize=(8, 5))

# Generate x values for the normal distribution curve
x_norm = np.linspace(-4, 4, 500)
y_norm = norm.pdf(x_norm, 0, 1) # Standard normal distribution (mean=0, std=1)
ax_conf_int.plot(x_norm, y_norm, label='Standard Normal Distribution')

# Shade the confidence interval area (assuming 95% CI, z-scores approx -1.96 and 1.96)
x_fill = np.linspace(-1.96, 1.96, 500)
y_fill = norm.pdf(x_fill, 0, 1)
ax_conf_int.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label='95% Confidence Interval')

ax_conf_int.set_title('Confidence Interval Visualization (Normal Distribution)')
ax_conf_int.set_xlabel('Z-score')
ax_conf_int.set_ylabel('Probability Density')
ax_conf_int.legend()
plt.savefig('spicy_food_preference_conf_interval.png')
print("\n")

# Visualize confidence interval for Pineapple Pizza Preference (Single Proportion - Yes) -  Conceptual Normal Distribution
n_pineapple_yes = pineapple_pizza_counts['Yes'] # Reusing existing count
n_pineapple_total = len(data) # Reusing existing total
conf_interval_pineapple_single = proportion_confint(n_pineapple_yes, n_pineapple_total, method='wilson') # Recalculating if needed, or reuse existing conf_interval_pineapple if you want single proportion CI

fig_conf_int_pineapple, ax_conf_int_pineapple = plt.subplots(figsize=(8, 5))

# Generate x values for the normal distribution curve
x_norm = np.linspace(-4, 4, 500)
y_norm = norm.pdf(x_norm, 0, 1) # Standard normal distribution (mean=0, std=1)
ax_conf_int_pineapple.plot(x_norm, y_norm, label='Standard Normal Distribution')

# Shade the confidence interval area (assuming 95% CI, z-scores approx -1.96 and 1.96)
x_fill = np.linspace(-1.96, 1.96, 500)
y_fill = norm.pdf(x_fill, 0, 1)
ax_conf_int_pineapple.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label='95% Confidence Interval')

ax_conf_int_pineapple.set_title('Confidence Interval Visualization (Pineapple Pizza Preference - Single Proportion - Conceptual Normal Distribution)') # Modified title
ax_conf_int_pineapple.set_xlabel('Z-score')
ax_conf_int_pineapple.set_ylabel('Probability Density')
ax_conf_int_pineapple.legend()
plt.savefig('pineapple_pizza_preference_conf_interval.png') # New file name
print("\n")

# Calculate gender-specific data for spicy food preference
male_data = data[data['Please select your gender'] == 'Male']
female_data = data[data['Please select your gender'] == 'Female']

male_spicy_yes = len(male_data[male_data['Do you like spicy food? (please choose one)'] == 'Yes'])
male_total = len(male_data)
female_spicy_yes = len(female_data[female_data['Do you like spicy food? (please choose one)'] == 'Yes'])
female_total = len(female_data)

# Confidence Interval for Difference in Spicy Food Preference Proportions between Genders
print("----------------------------------------")
print("Confidence Interval: Difference in Spicy Food Preference Proportions (Male - Female)")
prop_male_spicy = male_spicy_yes / male_total
prop_female_spicy = female_spicy_yes / female_total
diff_prop_spicy = prop_male_spicy - prop_female_spicy

pooled_prop_spicy = (male_spicy_yes + female_spicy_yes) / (male_total + female_total)
std_error_diff_spicy = np.sqrt(pooled_prop_spicy * (1 - pooled_prop_spicy) * (1/male_total + 1/female_total))

z_critical = 1.96  # for 95% confidence interval
margin_of_error_spicy = z_critical * std_error_diff_spicy
conf_interval_diff_spicy = (diff_prop_spicy - margin_of_error_spicy, diff_prop_spicy + margin_of_error_spicy)

print(f"Sample proportion of males who like spicy food: {prop_male_spicy:.4f}")
print(f"Sample proportion of females who like spicy food: {prop_female_spicy:.4f}")
print(f"Difference in proportions: {diff_prop_spicy:.4f}")
print(f"95% Confidence Interval for the difference: {conf_interval_diff_spicy}")
print("----------------------------------------\n")

# Two-Sample Z-Test for Spicy Food Preference by Gender
print("----------------------------------------")
print("Two-Sample Z-Test: Spicy Food Preference by Gender")

zstat_spicy, pvalue_spicy = proportions_ztest(
    [male_spicy_yes, female_spicy_yes],
    [male_total, female_total],
    alternative='two-sided'
)

print(f"Males who like spicy food: {male_spicy_yes} out of {male_total}")
print(f"Females who like spicy food: {female_spicy_yes} out of {female_total}")
print(f"Z-statistic: {zstat_spicy:.4f}, P-value: {pvalue_spicy:.4f}")

alpha = 0.05  # Significance level
if pvalue_spicy < alpha:
    print("Reject the null hypothesis: There is a significant difference in spicy food preference between genders.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in spicy food preference between genders.")
print("----------------------------------------\n")

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

# Calculate gender-specific data for pineapple preference
male_pineapple_yes = len(male_data[male_data['Do you like pineapples on your pizza (please choose one)'] == 'Yes'])
female_pineapple_yes = len(female_data[female_data['Do you like pineapples on your pizza (please choose one)'] == 'Yes'])

# Confidence Interval for Difference in Pineapple on Pizza Preference Proportions between Genders
print("----------------------------------------")
print("Confidence Interval: Difference in Pineapple on Pizza Preference Proportions (Male - Female)")
prop_male_pineapple = male_pineapple_yes / male_total
prop_female_pineapple = female_pineapple_yes / female_total
diff_prop_pineapple = prop_male_pineapple - prop_female_pineapple

pooled_prop_pineapple = (male_pineapple_yes + female_pineapple_yes) / (male_total + female_total)
std_error_diff_pineapple = np.sqrt(pooled_prop_pineapple * (1 - pooled_prop_pineapple) * (1/male_total + 1/female_total))

margin_of_error_pineapple = z_critical * std_error_diff_pineapple
conf_interval_diff_pineapple = (diff_prop_pineapple - margin_of_error_pineapple, diff_prop_pineapple + margin_of_error_pineapple)

print(f"Sample proportion of males who like pineapple on pizza: {prop_male_pineapple:.4f}")
print(f"Sample proportion of females who like pineapple on pizza: {prop_female_pineapple:.4f}")
print(f"Difference in proportions: {diff_prop_pineapple:.4f}")
print(f"95% Confidence Interval for the difference: {conf_interval_diff_pineapple}")
print("----------------------------------------\n")

# Two-Sample Z-Test for Pineapple on Pizza Preference by Gender
print("----------------------------------------")
print("Two-Sample Z-Test: Pineapple on Pizza Preference by Gender")
male_pineapple_yes = len(male_data[male_data['Do you like pineapples on your pizza (please choose one)'] == 'Yes'])
female_pineapple_yes = len(female_data[female_data['Do you like pineapples on your pizza (please choose one)'] == 'Yes'])

zstat_pineapple, pvalue_pineapple = proportions_ztest(
    [male_pineapple_yes, female_pineapple_yes],
    [male_total, female_total],
    alternative='two-sided'
)

print(f"Males who like pineapple on pizza: {male_pineapple_yes} out of {male_total}")
print(f"Females who like pineapple on pizza: {female_pineapple_yes} out of {female_total}")
print(f"Z-statistic: {zstat_pineapple:.4f}, P-value: {pvalue_pineapple:.4f}")

if pvalue_pineapple < alpha:
    print("Reject the null hypothesis: There is a significant difference in pineapple pizza preference between genders.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in pineapple pizza preference between genders.")
print("----------------------------------------\n")

print("Script completed. Output saved to script-output.txt and images saved as PNG files.")
