import urllib.request, urllib.parse, urllib.error
import json
import csv
import re

fields = []
rows = []
postal_codes = []

with open('IN.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",", quotechar = '"')
    fields = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
        # print(re.findall('^IN/([0-9]+)', row[0]))
        postal_codes.append(re.findall('^IN/([0-9]+)', row[0]))

    # print(postal_codes)

    zips = []

    for postal_code in postal_codes:
        for zip in postal_code:
            zips.append(zip)

    # print(zips)
    with open('code.csv', 'w') as file:
        csv_writer = csv.writer(file)
        for zip in zips:
            url = f"https://nominatim.openstreetmap.org/search.php?q={zip}&format=jsonv2"
            fhand = urllib.request.urlopen(url)
            data_json = json.loads(fhand.read())
            # print(data_json)
            key1 = "lat"
            key2 = "lon"
            li1 = [item.get(key1) for item in data_json]
            li2 = [item.get(key2) for item in data_json]
            if len(li1) == 0: 
                continue
            i=0
            while i<len(li1):
                if 8.06666<=float(li1[i])<=37.1 and 68.11666<=float(li2[i])<=97.41667:
                    coordinates = [li1[i], li2[i]]
                    print(coordinates)
                    csv_writer.writerow(coordinates)
                    break
                i+=1
            


