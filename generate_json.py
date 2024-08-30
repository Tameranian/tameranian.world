import os
import json

# Define the base directory and years to scan
base_dir = 'images'
years = ['2021', '2022', '2023', '2024']
data = {}

for year in years:
    year_dir = os.path.join(base_dir, year)
    if os.path.isdir(year_dir):
        # List all image files in the year directory and prepend "images/"
        images = [os.path.join(base_dir, year, img).replace(os.path.sep, '/') for img in os.listdir(year_dir) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        data[year] = images

# Write the data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('data.json has been generated.')
