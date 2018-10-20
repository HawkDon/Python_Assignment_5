import requests
import csv

def downloadcsv(url):
    data = requests.get(url)

    with open('uforeports.csv', "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        reader = csv.reader(data.text.splitlines())
        
        for row in reader:
            writer.writerow(row)

downloadcsv("https://raw.githubusercontent.com/planetsig/ufo-reports/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv")