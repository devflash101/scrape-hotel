# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
import json
import re

# Specify the URL you want to fetch
url = 'https://www.conference-hotel.com/home.php?Kundenid=1267006180&Listid=1&ts=1708492429&Language=US'
# Use requests to fetch the content of the URL
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title of the page
title = soup.title.text

with open('data.json', 'w') as file:
    totaldata = {}

# ------------------ hotel description
    hotel_description_data = {}
    hotel_description = soup.find(id='tabs-1').div.div

    hotel_description_data['url'] = url
    hotel_description_data['name'] = soup.find(class_="header_row bottom_row").div.h1.text
    hotel_description_data['hoteldescription_title'] = hotel_description.div.h1.text
    hotel_description_data['hoteldescription_description'] = hotel_description.div.p.text
    # ------------- hotel features
    hotel_features = hotel_description.find_all(class_="column_row")[1]
    hotel_features_li_buf = hotel_features.find_all('li')
    for i in range(1, len(hotel_features_li_buf)+1):
        li = hotel_features_li_buf[i-1]
        # print(li.text)
        key_string = 'hotelfeatures_' + str(i)
        hotel_description_data[key_string] = li.text
    # ------------- Safety Equipment
    safety_equipment = hotel_description.find_all(class_="column_row")[2]
    safety_equipment_li_buf = safety_equipment.find_all('li')
    for i in range(1, len(safety_equipment_li_buf)+1):
        li = safety_equipment_li_buf[i-1]
        # print(li.text)
        key_string = 'safetyequipment_' + str(i)
        hotel_description_data[key_string] = li.text
    # ------------- Room Features
    room_features = hotel_description.find_all(class_="column_row")[3]
    room_features_text = room_features.p.text
    room_features_numbers = re.findall(r'\d+', room_features_text)
    room_features_numbers = [int(num) for num in room_features_numbers]
    hotel_description_data['Total number of guest rooms'] = room_features_numbers[0]
    hotel_description_data['subdivided into'] = room_features_numbers[1]
    hotel_description_data['Junior Suites'] = room_features_numbers[2]
    hotel_description_data['Suites'] = room_features_numbers[3]

    room_features_li_buf = room_features.find_all('li')
    for i in range(1, len(room_features_li_buf)+1):
        li = room_features_li_buf[i-1]
        # print(li.text)
        key_string = 'roomfeatures_' + str(i)
        hotel_description_data[key_string] = li.text
    
    hotel_description_data['roomfeatures_description'] = room_features.find_all('p')[1].text
    # ------------- Food & Beverages
    food_beverages = hotel_description.find_all(class_="column_row")[4]
    food_beverages_li_buf = food_beverages.find_all('li')
    for i in range(1, len(food_beverages_li_buf)+1):
        li = food_beverages_li_buf[i-1]
        # print(li.text)
        key_string = 'foodbeverages_' + str(i)
        hotel_description_data[key_string] = li.text
    # ------------- Sport & Leisure at the hotel
    sport_leisure = hotel_description.find_all(class_="column_row")[5]
    sport_leisure_li_buf = sport_leisure.find_all('li')
    for i in range(1, len(sport_leisure_li_buf)+1):
        li = sport_leisure_li_buf[i-1]
        # print(li.text)
        key_string = 'sport-leisure_' + str(i)
        hotel_description_data[key_string] = li.text
    # ------------- Sport & Leisure in the area
    sport_leisure_area = hotel_description.find_all(class_="column_row")[6]
    sport_leisure_area_li_buf = sport_leisure_area.find_all('li')
    for i in range(1, len(sport_leisure_area_li_buf)+1):
        li = sport_leisure_area_li_buf[i-1]
        # print(li.text)
        key_string = 'sport-leisure_area_' + str(i)
        hotel_description_data[key_string] = li.text


# ------------------ Key Facts
    key_facts_data = {}
    key_facts = soup.find(id='tabs-1').div.find(class_='column_1 last')
    key_facts_data['No. of meeting rooms'] = int(key_facts.find_all(class_='dark')[0].span.text)
    key_facts_data['Capacity largest meeting room'] = key_facts.find_all(class_='light')[0].span.text
    key_facts_data['Space largest meeting room'] = key_facts.find_all(class_='dark')[1].span.text
    key_facts_data['No. of hotel rooms'] = key_facts.find_all(class_='light')[1].span.text
    key_facts_data['Distance to airport'] = key_facts.find_all(class_='dark')[2].span.text
    key_facts_data['Distance to motorway'] = key_facts.find_all(class_='light')[2].span.text
    key_facts_data['Distance to trade fair'] = key_facts.find_all(class_='dark')[3].span.text
    key_facts_data['No. of parking spaces'] = int(key_facts.find_all(class_='light')[3].span.text)
    key_facts_data['No. underground parking spaces'] = int(key_facts.find_all(class_='dark')[4].span.text)
    key_facts_data['Underground parking fees'] = key_facts.find_all(class_='light')[4].span.text

    key_facts_data['address_street'] = key_facts.find(class_='column_row address').text.split('\n')[2].strip()
    key_facts_data['address_postcode'] = int(key_facts.find(class_='column_row address').text.split('\n')[3].strip().split()[0])
    key_facts_data['address_city'] = key_facts.find(class_='column_row address').text.split('\n')[3].strip().split()[1]
    key_facts_data['address_country'] = key_facts.find(class_='column_row address').text.split('\n')[4].strip()

    key_facts_language_li_buf = key_facts.find(class_="column_row languages").find_all('li')
    # print(key_facts_language_li_buf)
    for i in range(1, len(key_facts_language_li_buf)+1):
        li = key_facts_language_li_buf[i-1]
        # print(li.text)
        key_string = 'languages_' + str(i)
        key_facts_data[key_string] = li.text

# ------------------ "Meeting Rooms" section
    meeting_rooms_data = {}
    meeting_rooms = soup.find(id='tabs-2')
    meeting_rooms_tbody_buf = meeting_rooms.div.table.find_all('tr', class_="light")

    table_col_names = ['name', 'size', 'U-shape', 'Conference', 'Rounds', 'Classroom', 'Theater', 'Reception', 'Circle of chairs']

    for i in range(0, len(meeting_rooms_tbody_buf)):
        key_string_demo = 'room_' + str(i+1) + '_'
        meeting_rooms_data[key_string_demo+'name'] = meeting_rooms_tbody_buf[i].td.text.split('\u00a0')[0].strip()
        for j in range(1, len(table_col_names)):
            key_string = key_string_demo + table_col_names[j]
            meeting_rooms_data[key_string] = meeting_rooms_tbody_buf[i].find_all('td', class_='')[j+6].text
        # print(meeting_rooms_tbody_buf[i].find_all('td', class_=""))

    # temp = soup.find(id="tabs-1").div.div.div.h1.text
    # print(temp)

    
    totaldata['hotel description'] = hotel_description_data
    totaldata['"Keyfacts" section'] = key_facts_data
    totaldata['"Meeting Rooms" section'] = meeting_rooms_data
    json.dump(totaldata, file, indent=4)

# Print the title
# print("The title of the page is:", title)
