import pandas as pd

df = pd.read_csv("./Raw_data/Joined_data/Waterford/combined_file_double_waterford.csv")

# Extract numerical value of "Price" column as int
df['Rent Price'] = df['prices'].str.extract('([\d,]+)').replace({',': ''}, regex=True).astype(int)

#extract frequency type (monthly|weekly) from second column
df['Frequency'] = df['prices'].str.extract('(monthly|weekly)')

# Save updated data frame if needed
#df.to_csv('updated_double_dublin.csv', index=False)

# Save the DataFrame to a new excel file
dublin_rent = df[['Rent Price', 'Frequency', 'address']]

dublin_rent.to_excel('Rent Waterford Double Room.xlsx', index=False)

print(df)