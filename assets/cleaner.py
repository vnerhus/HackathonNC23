import csv

input_file = 'ukemenu5til7clean.csv'
output_file = 'output.csv'

with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    for row in reader:
        new_row = ['"' + item + '"' for item in row]
        writer.writerow(new_row)