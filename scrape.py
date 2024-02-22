# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Specify the URL you want to fetch
url = 'https://www.tagungshotel.com/search_details.php?ts=1708518895&Language=EN'
cookies = {
    'PHPSESSID': 'og2fvdcmi9qn77f0fqoo4qj61h6c8njj7p1onk75crk3b2r36ih1'
}
# Use requests to fetch the content of the URL
response = requests.get(url, cookies=cookies)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the page
title = soup.title.text

all_p_elements = soup.find_all('p', class_="ContentSearchDetailsHotelTextHotel")

with open('switzerland.txt', 'w') as file:
    for p_element in all_p_elements:
        url = p_element.a.get('href')
        # print(url)
        file.write(url + '\n')

# Print the title
print("The title of the page is:", title)
