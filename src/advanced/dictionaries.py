dictionary = { "key": "value", "number": 42, "list": [1, 2, 3] }
print("Getting a dictionary value:", dictionary["key"])
dictionary["new_key"] = "new_value"
dictionary["number"] += 1
dictionary.pop("list")
print("Updated dictionary:", dictionary)
print("Checking for 'key' in dictionary:", "key" in dictionary)
print("Looping through dictionary keys:")
for key in dictionary:
    print("Key:", key)
print("Looping through dictionary values:")
for value in dictionary.values():
    print("Value:", value)
print("Looping through dictionary items:")
for key, value in dictionary.items():
    print("Key:", key, "Value:", value)
dictionary_copy = dictionary.copy()
print("Copied dictionary:", dictionary_copy)
print("Merging another dictionary:")
dictionary.update({ "new_key": "new_value", "number": 100 })
print("Merged dictionary:", dictionary)
