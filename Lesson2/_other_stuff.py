# Other stuff
# Modifying data in a file by changing US to United States while also getting its location in the file

import csv
"""
import pandas as pd

df = pd.read_csv("data/continents_2.csv")
df.head(3)
"""

with open("data/continents_2.csv") as file:
    reader = csv.reader(file)
    country_list = list(reader)
"""
index = 0
for country in country_list:
    if country == ['Africa', 'Angola']:
        country.insert(index(country), ['North America', 'United States'])
        #country = ['North America', 'United States']
"""


print(country_list)

