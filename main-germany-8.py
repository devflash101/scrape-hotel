import time
import pandas as pd
from hotel_data import getDataFromHotel


# Create lists to store data for each column
column_a = []
column_b = []
column_c = []

# Open the text file for reading
with open('germany-numbers-8.txt', 'r', encoding='utf-8') as file:
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

# # Write column_a to a text file
# with open('txt/column_a-8.txt', 'w', encoding='utf-8') as f_a:
#     for item in column_a:
#         f_a.write(f"{item}\n")

# # Write column_b to a text file
# with open('txt/column_b-8.txt', 'w', encoding='utf-8') as f_b:
#     for item in column_b:
#         f_b.write(f"{item}\n")

# # Write column_c to a text file
# with open('txt/column_c-8.txt', 'w', encoding='utf-8') as f_c:
#     for item in column_c:
#         f_c.write(f"{item}\n")

# Create DataFrame
df = pd.DataFrame({
    'Column A': column_a,
    'Column B': column_b,
    'Column C': column_c
})

# Define a function to clean the data
def clean_data(text):
    # Replace illegal characters with an empty string
    cleaned_text = ''.join(char for char in text if ord(char) < 128)
    return cleaned_text

# Clean the DataFrame
df['Column A'] = df['Column A'].apply(clean_data)
df['Column B'] = df['Column B'].apply(clean_data)
df['Column C'] = df['Column C'].apply(clean_data)

# Write DataFrame to Excel
df.to_excel('germany-8.xlsx', index=False)