import csv

input_file = './docs/data/spotify-2023.csv'
output_file = './docs/data/spotify-2023-artistas.csv'

with open(input_file, 'r', encoding='utf-8', errors='replace') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write the header for the output file
    writer.writerow(['track_name', 'artists', 'streams', 'released_year'])
    
    next(reader)  # Skip the header row
    for row in reader:
        track_name = row[0]
        artists = row[1].split(', ')
        streams = row[8]
        released_year = row[3]
        
        for artist in artists:
            writer.writerow([track_name,artist, streams, released_year])
