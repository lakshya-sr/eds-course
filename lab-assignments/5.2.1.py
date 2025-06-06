import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset from the CSV file
df = pd.read_csv('titanic.csv')

# Set up the figure for 5 subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

count_P=df["Pclass"].value_counts().sort_index()
count_G=df["Gender"].value_counts()
count_S=df["Survived"].value_counts().sort_index()

axes[0,0].bar(count_P.index,count_P.values,color=["skyblue"])
axes[0,0].set_title("Passenger Class Distribution")
axes[0,0].set_xlabel("Pclass")
axes[0,0].set_ylabel("Count")

axes[0,1].pie(count_G.values,labels=['male','female'],colors=['lightblue','lightcoral'],autopct='%1.1f%%')
axes[0,1].set_title('Gender Distribution')

axes[1,0].hist(df['Age'],color=['lightgreen'],edgecolor='black',bins=8)
axes[1,0].set_title('Age Distribution')
axes[1,0].set_xlabel("Age")
axes[1,0].set_ylabel("Frequency")

axes[1,1].bar(count_S.index,count_S.values,color=['lightblue','lightcoral'])
axes[1,1].set_title('Survival Count')
axes[1,1].set_xlabel('Survived(0=N0,1=Yes)')
axes[1,1].set_ylabel('Count')

axes[2,0].scatter(df['Age'],df['Fare'],color='orange')
axes[2,0].set_title('Fare vs Age')
axes[2,0].set_xlabel('Age')
axes[2,0].set_ylabel('Fare')
plt.tight_layout()
plt.show() 
