import json

personObject = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "swimming"]
}

personJSON = json.dumps(personObject, indent=4)
print("JSON Object:\n", personJSON)

with open("../data/person.json", "w") as jsonFile:
    json.dump(personObject, jsonFile, indent=4)

personObjectReparsed = json.loads(personJSON)
print("\nRe-parsed Object:", personObjectReparsed)

with open("../data/person.json", "r") as jsonFile:
    personFromFile = json.load(jsonFile)
    print("\nObject loaded from file:", personFromFile)


class Person:
    def __init__(self, name, age, city, hobbies):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = hobbies


personInstance = Person("Jane", 25, "Los Angeles", ["dancing", "cooking"])
personInstanceJSON = json.dumps(personInstance.__dict__, indent=4)
print("\nPerson Instance JSON:\n", personInstanceJSON)
