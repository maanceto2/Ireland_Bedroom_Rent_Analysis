import pandas as pd 

df = pd.read_csv('./Raw_data/Joined_data/Waterford/combined_file_double_waterford.csv.csv')

# Extract numerical value from prices column as an int 
df['Rent Price'] = df['prices'].str.extract('([\d,]+)').replace({',': ''}, regex=True).astype(int)

# Extract frequency from price column 
df['Frequency'] = df['prices'].str.extract('(monthly|weekly)')

# Save the DataFrame to a new excel and csv file

rent = df[['Rent Price', 'Frequency', 'address']]

rent.to_csv('Rent.csv', index=False)
rent.to_excel('Rent.xlsx', index=False)

print(rent)