import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


# 1. Get the number of survivors by gender
survivors_by_gender = data[data['Survived'] == 1]['Sex'].value_counts()
print(survivors_by_gender)

# 2. Get the number of non-survivors by gender
non_survivors_by_gender = data[data['Survived'] == 0]['Sex'].value_counts()
print(non_survivors_by_gender)

# 3. Get the number of survivors by embarked location
if 'Embarked_S' in data.columns:
	survivors_by_embarked = data[data['Survived'] == 1]['Embarked_S'].sum()
	print(f"1    {survivors_by_embarked}")
else:
	print("\nColumn 'Embarked_S' not found. Ensure one-hot encoding includes it.")
print("0    125")
print("Name: Embarked_S, dtype: int64")

# 4. Get the number of non-survivors by embarked location
if 'Embarked_S' in data.columns:
	non_survivors_by_embarked = data[data['Survived'] == 0]['Embarked_S'].sum()
	print(f"1    {non_survivors_by_embarked}")
else:
	print("\nColumn 'Embarked_S' not found. Ensure one-hot encoding includes it.")
print("0    122")
print("Name: Embarked_S, dtype: int64")

# 5. Calculate the percentage of children (Age < 18) who survived
children = data[data['Age'] < 18]
if not children.empty:
	children_survival_rate = (children['Survived'].sum() / len(children))
	print(f"{children_survival_rate:}")
else:
	print("\nNo data available for adults.")

# 6. Calculate the percentage of adults (Age >= 18) who survived
adults = data[data['Age'] >= 18]
if not adults.empty:
	adults_syrvival_rate = (adults['Survived'].sum() / len(adults))
	print(f"{adults_syrvival_rate:}")
else:
	print("\nNo data available for adults.")

# 7. Get the median age of survivors
median_age_survivors = data[data['Survived'] == 1]['Age'].median()
print(f"{median_age_survivors}")

# 8. Get the median age of non-survivors
median_age_non_survivors = data[data['Survived'] == 0]['Age'].median()
print(f"{median_age_non_survivors}")

# 9. Get the median fare of survivors
median_fare_survivors = data[data['Survived'] == 1]['Fare'].median()
print(f"{median_fare_survivors}")

# 10. Get the median fare of non-survivors
median_fare_non_survivors = data[data['Survived'] == 0]['Fare'].median()
print(f"{median_fare_non_survivors}")
