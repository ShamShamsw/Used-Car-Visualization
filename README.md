# Used-Car-Visualization

This project visualizes data from a used car dataset to provide insights into pricing, mileage, fuel types, and other factors. The visualizations are generated using Python libraries such as `pandas`, `seaborn`, and `matplotlib`.

## Features

1. **Data Cleaning**:
   - Handles missing values in critical columns.
   - Ensures numeric columns are properly formatted.
   - Drops rows with invalid numeric values.

2. **Visualizations**:
   - **Boxplot of Price by Brand**: Displays the price distribution for the top 10 car brands.
   - **Scatter Plot: Mileage vs. Price**: Shows the relationship between mileage and price with a regression line.
   - **Bar Chart: Average Price by Fuel Type**: Highlights the average price for different fuel types using a rainbow color palette.
   - **Pie Chart: Clean Title vs Salvage**: Compares the proportion of clean titles to salvage titles.
   - **Pie Chart: Accidents vs No Accidents**: Visualizes the proportion of cars with and without accident history.
   - **Heatmap of Variable Correlations**: Displays correlations between numeric variables such as price, mileage, model year, and engine size.
   - **Violin Plot: Price vs Transmission**: Shows the distribution of prices based on transmission type.

3. **Image Export**:
   - All visualizations are saved as high-resolution images in the `images` folder.

## Prerequisites

- Python 3.7 or higher
- Required libraries:
  - `pandas`
  - `seaborn`
  - `matplotlib`
  - `numpy`

Install the required libraries using pip:

```bash
pip install pandas seaborn matplotlib numpy