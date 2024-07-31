import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'IndividualID': range(1, 21),
    'SmokingHabits': [5, 20, 15, 0, 10, 30, 25, 0, 0, 35, 5, 15, 10, 20, 25, 5, 10, 0, 15, 20],
    'LungCancerIncidence': [1, 3, 2, 0, 1, 4, 3, 0, 0, 5, 1, 2, 1, 3, 3, 1, 1, 0, 2, 3]
}
df = pd.DataFrame(data)
correlation = df['SmokingHabits'].corr(df['LungCancerIncidence'])
print(f"Correlation Coefficient: {correlation:.3f}")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SmokingHabits', y='LungCancerIncidence', data=df, s=100, color='blue', edgecolor='w')
plt.title('Scatter Plot of Smoking Habits vs. Lung Cancer Incidence')
plt.xlabel('Smoking Habits (Cigarettes per day)')
plt.ylabel('Lung Cancer Incidence')
plt.grid(True)
plt.show()
