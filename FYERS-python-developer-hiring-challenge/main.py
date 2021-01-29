# import packages
import csv
import json

csvFilePath = 'csv/airlines.csv'
jsonFilePath = 'json/airlines.json'

# create dictionary
data = {}

# read csv file and add data to 'data'
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        airportName = rows['Airport.Name']
        if airportName not in data:
            data[airportName] = 0
        data[airportName] = data[airportName] + 1

# create json file and write data on it
with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

# Name and count of the airport which is mentioned the most number of time
maxCount = max(data, key=data.get)
print("Max Count => " + maxCount, data[maxCount])

# Name and count of the airport which is mentioned the least number of time
minCount = min(data, key=data.get)
print("Least Count => " + minCount, data[minCount])