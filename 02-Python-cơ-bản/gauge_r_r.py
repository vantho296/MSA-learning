import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the random seed for reproducibility
np.random.seed(42)

# Data generation parameters
num_parts = 30  # Number of parts
num_measures = 3  # Number of measurements per part
num_operators = 2  # Number of operators

# Generate part measurements
parts = np.repeat(np.arange(1, num_parts + 1), num_measures * num_operators)
operators = np.tile(np.repeat(np.arange(1, num_operators + 1), num_measures), num_parts)
measurements = np.random.normal(loc=50, scale=5, size=num_parts * num_measures * num_operators)

df = pd.DataFrame({'Part': parts, 'Operator': operators, 'Measurement': measurements})

# Calculate Repeatability (within operator variation)
repeatability = df.groupby('Operator')['Measurement'].std().mean()

# Calculate Reproducibility (between operator variation)
operator_means = df.groupby('Operator')['Measurement'].mean()
reproducibility = operator_means.std()

# Print results
print(f'Repeatability: {repeatability:.2f}')
print(f'Reproducibility: {reproducibility:.2f}')

# Visualization
plt.figure(figsize=(12, 6))
# Boxplot of measurements by operator
sns.boxplot(x='Operator', y='Measurement', data=df)
plt.title('Measurement Distribution by Operator')
plt.ylabel('Measurement Values')
plt.xlabel('Operator')
plt.axhline(df['Measurement'].mean(), color='red', linestyle='--', label='Overall Mean')
plt.legend()
plt.show()