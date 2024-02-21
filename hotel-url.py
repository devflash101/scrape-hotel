import time

# Open the text file for reading
with open('germany.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Print the current line to the console
        # print(line.strip())  # .strip() removes the newline character at the end
        url = 'https://www.conference-hotel.com/' + line.strip()
        print(url)
        # Wait for 1 second before proceeding to the next line
        time.sleep(1)