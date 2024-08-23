import pandas as pd 
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import numpy as np

#Load data
file_path = 'C:/Users/Marcos Neto/Documents/GitHub/Ireland_Bedroom_Rent_Analysis/Raw_data/Joined_data/Dublin/Dublin_Double_Rent.xlsx'
df = pd.read_excel(file_path)

#print(df.head())

# Define grid size
grid_size = 100

# Create a 2D histogram for the heatmap
heatmap, xedges, yedges = np.histogram2d(df['Latitude'], df['Longitude'], bins=grid_size, weights=df['Rent Monthly'])

# Create meshgrid
X, Y = np.meshgrid(xedges, yedges)

# Plot using pcolormesh
plt.figure(figsize=(10, 8))
plt.pcolormesh(X, Y, heatmap.T, cmap='coolwarm')
plt.colorbar(label='Monthly Rent')
plt.title('Rental Price Heatmap Double Room Dublin')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Create a base map centered around the mean latitude and longitude
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=13)

# Prepare data for HeatMap
heat_data = [[row['Latitude'], row['Longitude'], row['Rent Monthly']] for index, row in df.iterrows()]

# Add the heatmap layer
HeatMap(heat_data).add_to(m)

# Save the map to an HTML file or display it
m.save('rental_heatmap.html')
m