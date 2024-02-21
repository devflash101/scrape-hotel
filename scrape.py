# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Specify the URL you want to fetch
url = 'https://www.conference-hotel.com/search_details.php?ts=1708492387&Language=US'
cookies = {
    'PHPSESSID': '6mtc5spv94c7soa7drv5sbkhvg2ou2kjfvkkaa94r1u2pjci9hj0'
}
# Use requests to fetch the content of the URL
response = requests.get(url, cookies=cookies)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the page
title = soup.title.text

all_p_elements = soup.find_all('p', class_="ContentSearchDetailsHotelTextHotel")

with open('germany.txt', 'w') as file:
    for p_element in all_p_elements:
        url = p_element.a.get('href')
        # print(url)
        file.write(url + '\n')

# Print the title
print("The title of the page is:", title)
