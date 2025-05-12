import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Calculate the survival rate by class
survival_rate_by_class = data.groupby('Pclass')['Survived'].mean()
print(survival_rate_by_class)

# 2. Calculate the survival rate by embarked location
if 'Embarked_S' in data.columns:
	survival_rate_by_embarked = data.groupby('Embarked_S')['Survived'].mean()
	print(survival_rate_by_embarked)
else:
	print("\nColumn 'Embarked_S' not found. Ensure one-hot encoding includes it.")
	
# 3. Calculate the survival rate by family size
survival_rate_by_family_size = data.groupby('FamilySize')['Survived'].mean()
print(survival_rate_by_family_size)

# 4. Calculate the survival rate by being alone
survival_rate_by_is_alone = data.groupby('IsAlone')['Survived'].mean()
print(survival_rate_by_is_alone)

# 5. Get the average fare by class
average_fare_by_class = data.groupby('Pclass')['Fare'].mean()
print(average_fare_by_class)

# 6. Get the average age by class
average_age_by_class = data.groupby('Pclass')['Age'].mean()
print(average_age_by_class)

# 7. Get the average age by survival status
average_age_by_survival = data.groupby('Survived')['Age'].mean()
print(average_age_by_survival)

# 8. Get the average fare by survival status
average_fare_by_survival = data.groupby('Survived')['Fare'].mean()
print(average_fare_by_survival)

# 9. Get the number of survivors by class
survivors_by_class = data[data['Survived'] == 1]['Pclass'].value_counts()
print(survivors_by_class)

# 10. Get the number of non-survivors by class
non_survivors_by_class = data[data['Survived'] == 0]['Pclass'].value_counts()
print(non_survivors_by_class)
