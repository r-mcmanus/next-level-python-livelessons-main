import csv
import os


with open("data/continents_3.csv") as infile, open('data/continents_3_temp.csv', 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, lineterminator='\n')
    for line in reader:
        if line == ['Africa', 'Angola']:
            line = writer.writerow(['AFRICA', 'ANGOLA'])
            break
        else:
            writer.writerow(line)
    writer.writerows(reader)

os.remove('data/continents_3.csv')
os.rename('data/continents_3_temp.csv', 'data/continents_3.csv')


