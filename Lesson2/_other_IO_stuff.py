# Other stuff
# Modifying data in a file by changing US to United States while also getting its location in the file

import csv
import os

country_list = []
with open("data/continents_2.csv") as file:
    reader = csv.reader(file)
    country_list = list(reader)


index = -1

for i, country in enumerate(country_list):
    if country == ['North America', 'US']:
        country_list[i] = ['North America', 'United States']
        index = i

if index != -1:
    print(f'The file was modified at row {index}.')
else:
    print('Country not found.')



#creating a file and writing to it.
with open("data/continents_2.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\n')
    for country in country_list:
        writer.writerow(country)
#apppending data
    writer.writerow(['Antarctica', 'Antarctica'])




print(country_list)

