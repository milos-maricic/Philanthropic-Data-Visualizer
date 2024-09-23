# Philanthropic Data Visualizer

This tool helps philanthropic organizations visualize the impact of their donations. It generates bar charts, time series plots, and heatmaps to display donation amounts by region, trends over time, and geographic distribution.

## Features
- **Bar Chart by Region**: Displays total donations by region.
- **Time Series Plot**: Shows donation trends over time.
- **Heatmap by Region**: Visualizes donation intensity across regions.

## How It Works
1. **Input Data**: Upload a CSV file containing columns for `region`, `amount`, and `date`.
2. **Visualization**: The tool creates visual insights such as total donations by region, trends over time, and a heatmap showing donation distributions.

## Example Usage
```python
# Example data for testing
data = pd.DataFrame({
    'region': ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Europe', 'Asia', 'Africa'],
    'amount': [50000, 30000, 45000, 20000, 25000, 40000, 30000, 5000],
    'date': ['2023-01-10', '2023-02-15', '2023-03-20', '2023-01-25', '2023-04-10', '2023-02-18', '2023-03-30', '2023-05-15']
})

# Visualize donations by region
visualize_donations_by_region(data)

# Visualize donations over time
visualize_donations_over_time(data)

# Visualize donations heatmap by region
visualize_donations_heatmap(data)
```

## Requirements
- Python 3.x
- Libraries: `pandas`, `matplotlib`

To install dependencies:
```bash
pip install pandas matplotlib
```

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Feel free to submit issues or pull requests for improvements!
