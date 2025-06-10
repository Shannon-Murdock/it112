import json

#
data1 = {
    'name': 'Shannon Murdock',
    'age': 51,
    'city': 'Seattle, WA',
    'interests': ['Writing', 'Graphic Art', 'Travel', 'Web Design', 'Baking', 'Kirigami'],
    'is_student': True
}

#Create a JSON file and write the python object contents to it
with open('data1.json', 'w') as json_file:
    json.dump(data1,json_file,indent=4)

print("Data was successfully written to data1.json")
