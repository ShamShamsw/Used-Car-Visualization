import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np

# Ensure the images folder exists
os.makedirs('images', exist_ok=True)

# Load the Excel file
file_path = r"dataset/testdatasetusedcar.xlsx"
data = pd.read_excel(file_path)

# Data Cleaning
# Drop rows with missing values in critical columns
data.dropna(subset=['price', 'brand', 'milage', 'fuel_type', 'model_year', 'clean_title', 'transmission'], inplace=True)

# Ensure numeric columns are of the correct type
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data['milage'] = pd.to_numeric(data['milage'], errors='coerce')
data['model_year'] = pd.to_numeric(data['model_year'], errors='coerce')
data['engine'] = pd.to_numeric(data['engine'], errors='coerce')

# Drop rows with invalid numeric values
data.dropna(subset=['price', 'milage', 'model_year', 'engine'], inplace=True)

# 2. Boxplot of Price by Brand (Top 10 Brands by Frequency)
top_brands = data['brand'].value_counts().head(10).index
filtered_data = data[data['brand'].isin(top_brands)]
plt.figure(figsize=(12, 6))
sns.boxplot(x='brand', y='price', data=filtered_data, order=top_brands)
plt.title('Boxplot of Price by Brand (Top 10 Brands)')
plt.xlabel('Brand')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.savefig('images/boxplot_price_by_brand.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Scatter Plot: Mileage vs. Price with Regression Line
plt.figure(figsize=(10, 6))
sns.regplot(x='milage', y='price', data=data, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Scatter Plot: Mileage vs. Price')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.savefig('images/scatter_mileage_vs_price.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Bar Chart: Average Price by Fuel Type (Rainbow Colors)
fuel_mapping = {1: 'Gasoline', 2: 'Diesel', 3: 'Electric', 4: 'Hybrid', 5: 'CNG', 6: 'LPG', 7: 'Other'}
data['fuel_type'] = data['fuel_type'].map(fuel_mapping)
avg_price_by_fuel = data.groupby('fuel_type')['price'].mean().sort_values()
plt.figure(figsize=(10, 6))
colors = sns.color_palette("rainbow", len(avg_price_by_fuel))
avg_price_by_fuel.plot(kind='bar', color=colors)
plt.title('Average Price by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.savefig('images/avg_price_by_fuel_type.png', dpi=300, bbox_inches='tight')
plt.show()

# 5. Pie Chart: Clean Title vs Salvage
clean_title_counts = data['clean_title'].value_counts()
labels = ['Clean Title', 'Salvage']
plt.figure(figsize=(8, 8))
plt.pie(clean_title_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'salmon'])
plt.title('Clean Title vs Salvage')
plt.savefig('images/clean_title_vs_salvage.png', dpi=300, bbox_inches='tight')
plt.show()

# 6. Heatmap of Variable Correlations
numeric_columns = ['price', 'milage', 'model_year', 'engine']
correlation_matrix = data[numeric_columns].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Variable Correlations')
plt.savefig('images/heatmap_variable_correlations.png', dpi=300, bbox_inches='tight')
plt.show()

# Optional: Violin Plot of Price vs Transmission
plt.figure(figsize=(10, 6))
sns.violinplot(x='transmission', y='price', data=data)
plt.title('Violin Plot: Price vs Transmission')
plt.xlabel('Transmission')
plt.ylabel('Price')
plt.savefig('images/violin_plot_price_vs_transmission.png', dpi=300, bbox_inches='tight')
plt.show()