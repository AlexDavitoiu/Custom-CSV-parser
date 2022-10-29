import csv
import hashlib


with open('rockyou-md5.csv', encoding= "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    line_count = 0
    for row in csv_reader:
        hash = hashlib.md5(row[0].encode('utf-8')).hexdigest()
        row.append(":" + hash)
            
           # print(row[1]) # + ":" + row[0])
           # line_count += 1
    print(f'Processed {line_count} lines.')