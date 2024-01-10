import requests
import re

url = "https://hotscope.tv/search/transsexual?page=1"

response = requests.get(url)
html_content = response.text

# Use regex to find all values of "id"
id_values = re.findall(r'"id":(\d+)', html_content)

# Save the values to values.txt
with open('values.txt', 'w') as file:
    for value in id_values:
        file.write(value + '\n')

print("Values extracted and saved to values.txt")
