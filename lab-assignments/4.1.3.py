
import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])
print("First five rows:")
print(data.head(5))
print("Average age:", data['Age'].mean().round(2))
print("Students with a grade up to B")
print(data[(data['Grade'] == 'A') | (data['Grade'] == 'B')])
# write your code here..

