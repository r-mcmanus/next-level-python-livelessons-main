"""
A program that takes a letter and prints
all of the countries that start with that letter
"""

# Todo: Read data/countries.txt and save all countries
countries = []
with open("data/countries.txt") as file:
    for line in file.readlines():
        countries.append(line.strip())

print(countries)
# Get user to provide a letter
letter = input('Number of countries that start with letter: ')
letter = letter.capitalize()

# Todo: Print the number of countries that start with the letter
letter_countries = []
for country in countries:
    if country[0] == letter:
        letter_countries.append(country)

print(f"{len(letter_countries)} countries start with the letter {letter}.")
# Todo: Print the countries that start with the letter
print(letter_countries)