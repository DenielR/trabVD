import csv

input_file = './docs/data/spotify-2023.csv'
output_file = './docs/data//spotify-2023-limpo.csv'

with open(input_file, 'r', encoding='utf-8', errors='replace') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        writer.writerow(row)
