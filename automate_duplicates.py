import csv

from sympy import false, true
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# import Levenshtein
def with_levenshtein(z, y):
    for i in y:
        if fuzz.WRatio(z, i) == 100:
            return false
    return true

with open('org_data_no_duplicates_2.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    with open('All_Organizations.csv', 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        writer.writerow(['Organization Id',	'Name',	'Website',	'Last Email',	'CB Location - Not available for export',	'CB Industry - Not available for export	Source of Introduction (Full Name)',	'Source of Introduction (Email)'	,'CB Year Founded - Not available for export',	'First Email',	'Type of Business',	'Lists',	'Phone Number'])
        names = []
        for row in reader:
            if row['Name'] not in names:
                if with_levenshtein(row['Name'], names):
                    names.append(row['Name'])
                    writer.writerow(row.values())
                else: 
                    continue
            else:
                continue



    
    