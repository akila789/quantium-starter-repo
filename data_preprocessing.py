import csv
import os
import glob

if os.path.exists('merged_file.csv'):
    os.remove('merged_file.csv')

csv_file_list = glob.glob('data\\*.csv')
output_file = 'merged_file.csv'

with open(output_file, mode='w', newline='') as out_file:
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(['Sales','Date','Region'])

    for file in csv_file_list:
        with open(file, mode='r') as src_file:
            csv_reader = csv.reader(src_file)
            next(csv_reader)
            for row in csv_reader:
                if row[0] == 'pink morsel':
                    csv_writer.writerow([float(row[1].replace('$',''))* int(row[2]), row[3],row[4]])
                    
