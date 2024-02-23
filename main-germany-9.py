import time
import pandas as pd
from hotel_data import getDataFromHotel


# Create lists to store data for each column
column_a = []
column_b = []
column_c = []

# Open the text file for reading
with open('germany-numbers-9.txt', 'r') as file:
    # Iterate over each line in the file
    cnt = 0
    for line in file:
        # Print the current line to the console
        # print(line.strip())  # .strip() removes the newline character at the end
        url = 'https://www.tagungshotel.com/home.php?Kundenid=' + line.strip()
        cnt += 1
        print(cnt)
        print(url)
        # Wait for 1 second before proceeding to the next line
        # time.sleep(1)
        hotel_data = getDataFromHotel(url)
        # Populate lists with JSON data
        for section, section_data in hotel_data.items():
            column_a.append(section)  # Append section name only once
            for key, value in section_data.items():
                column_a.append('')
                column_b.append(key)
                column_c.append(value)
            column_a.pop()
        column_a.append('')
        column_b.append('')
        column_c.append('')

# Create DataFrame
df = pd.DataFrame({
    'Column A': column_a,
    'Column B': column_b,
    'Column C': column_c
})

# Write DataFrame to Excel
df.to_excel('germany-9.xlsx', index=False)