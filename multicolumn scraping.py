import requests 
from bs4 import BeautifulSoup
import pandas as pd 

# Step 1: Send a GET request to the website
url = "https://www.rent.ie/rooms-to-rent/renting_dublin/room-type_double/page_27/"
response = requests.get(url)

# Step 2: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all the listings and extract the required information
prices = []
available_dates = []
addresses = []

# Find all div tags with class "sresult_description"
divs = soup.find_all('div', class_='sresult_description')

for div in divs:
    # Find the h4 tag within the div for the price
    price_tag = div.find('h4')
    if price_tag:
        price_text = price_tag.get_text(strip=True)
        prices.append(price_text)
    else:
        prices.append(None)
    
    # Find the text after the <br> tag for the available date
    br_tag = div.find('br')
    if br_tag:
        available_text = br_tag.next_sibling.strip() if br_tag.next_sibling else None
        available_dates.append(available_text)
    else:
        available_dates.append(None)

    # Find the address within the div with class "sresult_address"
    address_div = div.find_previous('div', class_='sresult_address')
    if address_div:
        address_tag = address_div.find('a')
        if address_tag:
            address_text = address_tag.get_text(strip=True)
            addresses.append(address_text)
        else:
            addresses.append(None)
    else:
        addresses.append(None)


# Step 4: Create a DataFrame from the scraped data
data = {
    'prices': prices,
    'available': available_dates,
    'address': addresses
}
df = pd.DataFrame(data)

# Step 5: Save the DataFrame to a CSV file
df.to_csv('rent_data_double27.csv', index=False)

print("Data has been saved")