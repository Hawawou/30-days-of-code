# read csv file to a dictionary

import csv

with open("birth.txt", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row["name"]} works in the {row["department"]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
