import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the Excel file
file_path = r"/dataset/testdatasetusedcar.xlsx"
data = pd.read_excel(file_path)

# 2. Boxplot of Price by Brand (Top 10 Brands by Frequency)
top_brands = data['brand'].value_counts().head(10).index
filtered_data = data[data['brand'].isin(top_brands)]
plt.figure(figsize=(12, 6))
sns.boxplot(x='brand', y='price', data=filtered_data, order=top_brands)
plt.title('Boxplot of Price by Brand (Top 10 Brands)')
plt.xlabel('Brand')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()

# 3. Scatter Plot: Mileage vs. Price with Regression Line
plt.figure(figsize=(10, 6))
sns.regplot(x='milage', y='price', data=data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Scatter Plot: Mileage vs. Price')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.show()

# 4. Bar Chart: Average Price by Fuel Type
fuel_mapping = {1: 'Gasoline', 2: 'Diesel', 3: 'Electric', 4: 'Hybrid', 5: 'CNG', 6: 'LPG', 7: 'Other'}
data['fuel_type'] = data['fuel_type'].map(fuel_mapping)
avg_price_by_fuel = data.groupby('fuel_type')['price'].mean().sort_values()
plt.figure(figsize=(10, 6))
avg_price_by_fuel.plot(kind='bar', color='skyblue')
plt.title('Average Price by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()

# 5. Pie Chart: Clean Title vs Salvage
clean_title_counts = data['clean_title'].value_counts()
labels = ['Clean Title', 'Salvage']
plt.figure(figsize=(8, 8))
plt.pie(clean_title_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'salmon'])
plt.title('Clean Title vs Salvage')
plt.show()

# 6. Histogram of Model Year
plt.figure(figsize=(10, 6))
bins = range(1996, 2026, 2)
plt.hist(data['model_year'], bins=bins, color='skyblue', edgecolor='black')
plt.title('Histogram of Model Year')
plt.xlabel('Model Year')
plt.ylabel('Frequency')
plt.xticks(bins, rotation=45)
plt.show()

# 7. Heatmap of Variable Correlations
numeric_columns = ['price', 'milage', 'model_year', 'engine']
correlation_matrix = data[numeric_columns].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Variable Correlations')
plt.show()

# Optional: Violin Plot of Price vs Transmission
plt.figure(figsize=(10, 6))
sns.violinplot(x='transmission', y='price', data=data)
plt.title('Violin Plot: Price vs Transmission')
plt.xlabel('Transmission')
plt.ylabel('Price')
plt.show()