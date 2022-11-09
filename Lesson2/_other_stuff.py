# Other stuff
# Modifying data in a file by changing US to United States while also getting its location in the file

import csv

country_list = []
with open("data/continents.csv") as file:
    reader = csv.reader(file)
    country_list = list(reader)


for i, country in enumerate(country_list):
    if country == ['North America', 'US']:
        country_list[i] = ['North America', 'United States']


print(country_list)

