
import json
# Valid JSON String in Python
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusmail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
data = json.loads(people_string) # creates a python dictionary from JSON

#  This prints the person in the data object that was created
#for person in data['people']:
#    print(person)
# print the name of the person from the person list
#for person in data['people']:
#    print (person['name'])

# deletes phone number from the dictionary
# dictionaries have {key:value} pairs
# lists are contained in [] brackets with string, numbers etc seperated by commas
for person in data['people']:
    del person['phone']
new_string = json.dumps(data)
print(new_string)