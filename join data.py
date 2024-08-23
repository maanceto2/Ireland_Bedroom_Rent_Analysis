import pandas as pd
import os

# Specify the folder where the CSV files are located
folder_path = 'C:/Users/Marcos Neto/Documents/GitHub/Ireland_Bedroom_Rent_Analysis/Raw_data/Cork_Rent/Single'

# Create a list of CSV file paths
csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

# Initialize an empty list to hold the DataFrames
df_list = []

# Loop through the list of files and read each one into a DataFrame, then append it to the list
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_file_single_cork.csv', index=False)