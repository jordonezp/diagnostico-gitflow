import json

with open('farmers-protest-tweets-2021-03-5.json') as file:
  data = json.load(file.read())
  print(data[0])
