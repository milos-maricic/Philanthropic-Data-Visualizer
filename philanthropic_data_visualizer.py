
import pandas as pd
import matplotlib.pyplot as plt

# Function to visualize donation data by amount and region
def visualize_donations_by_region(data):
    """
    Creates a bar chart to visualize total donations by region.
    :param data: DataFrame containing donation data with 'region' and 'amount' columns.
    """
    donations_by_region = data.groupby('region')['amount'].sum()
    
    plt.figure(figsize=(10, 6))
    donations_by_region.plot(kind='bar', color='skyblue')
    plt.title('Total Donations by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Amount Donated')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to visualize donations over time
def visualize_donations_over_time(data):
    """
    Creates a time-series plot to visualize donation trends over time.
    :param data: DataFrame containing donation data with 'date' and 'amount' columns.
    """
    data['date'] = pd.to_datetime(data['date'])
    donations_by_date = data.groupby('date')['amount'].sum()
    
    plt.figure(figsize=(10, 6))
    donations_by_date.plot(kind='line', marker='o', color='green')
    plt.title('Donations Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Amount Donated')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to create a heatmap of donations by region
def visualize_donations_heatmap(data):
    """
    Creates a heatmap (for example, using color intensity) of donations by region.
    :param data: DataFrame containing donation data with 'region' and 'amount' columns.
    """
    region_data = data.groupby('region')['amount'].sum()
    plt.figure(figsize=(8, 4))
    region_data.plot(kind='barh', color='red', alpha=0.6)
    plt.title('Heatmap of Donations by Region')
    plt.xlabel('Total Amount Donated')
    plt.tight_layout()
    plt.show()

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
