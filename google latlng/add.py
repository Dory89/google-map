import geocoder
import csv

l=[]
with open('add.csv','rt') as csvfile:
    reader = csv.DictReader(csvfile)
    columns=[row['address']for row in reader]
    print(columns)
    for i in columns:      
        g = geocoder.arcgis(i)
        l.append(g.latlng)
    with open('add.csv', 'a', newline='') as f:
        print(l)