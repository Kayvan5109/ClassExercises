import pandas as pd
import matplotlib.pyplot as plt
import json

dict1 = {
  "name": "John",
  "age": 30,
  "married": True,
  "children": [

    {"name": "Jenny", "age": 4},

    {"name": "Billy", "age": 2}

  ],
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#1. Assign the JSON data given above to a python variable and print the data (also with proper indentation).
print(dict1)
print(json.dumps(dict1, indent = 4))
print(dict1['name'])

#2. Retrieve and print the model name of the car that has mpg > 25.
for car in dict1['cars']:
  if car['mpg'] > 25:
    print(car['model'])

#3. Check if John is married and if yes, print the ages of his children.
if dict1["married"] == True:
  for child in dict1["children"]:
    print(child['age'])
    
#4. Modify the age of Jenny from 4 to 5 and save the entire data to a json file: john.json
for child in dict1["children"]:
  if child['name'] == 'Jenny':
    child["age"] = 5 

print(json.dumps(dict1, indent = 4))
with open("john.json", 'w') as f:
  json.dump(dict1, f, indent = 4)
 
#reading in json file
with open ('john.json') as f:
  dict1 = json.load(f)
  print(json.dumps(dict1, indent=4))

#5. Now, read the json file john.json, delete John's age information from the data and save the data to file: john2.json
with open ('john.json') as f:
  dict1 = json.load(f)
  print(json.dumps(dict1, indent=4))
  del dict1['age']
  with open ('john2.json', 'w') as f:
    json.dump(dict1, indent=4)