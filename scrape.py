import re

# Open the file in read mode with UTF-8 encoding
with open('switzerland-urls.txt', 'r', encoding='utf-8') as file:
    # Read the content of the text file
    text = file.read()

# Use regular expression to find numbers within favcart[] array
numbers = re.findall(r'favcart\[\'(\d+)\']', text)

print(len(numbers))

# Open a new file to write the numbers
with open('switzerland-numbers.txt', 'w') as output_file:
    # Write each number to the output file
    for number in numbers:
        output_file.write(number + '\n')

print("Numbers have been extracted and written to numbers.txt file.")
