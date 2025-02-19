import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()

# Create spicy food preference bar chart
spicy_food_counts = data['Do you like spicy food? (please choose one)'].value_counts()
plt.figure(figsize=(8, 6))
spicy_food_counts.plot(kind='bar')
plt.title('Spicy Food Preference')
plt.xlabel('Likes Spicy Food?')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=0)
plt.show()

# Create pineapple on pizza preference bar chart
pineapple_pizza_counts = data['Do you like pineapples on your pizza (please choose one)'].value_counts()
plt.figure(figsize=(8, 6))
pineapple_pizza_counts.plot(kind='bar')
plt.title('Pineapple on Pizza Preference')
plt.xlabel('Likes Pineapple on Pizza?')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=0)
plt.show()
