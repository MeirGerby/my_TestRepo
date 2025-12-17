
print(person["city"])
person["job"] = "Programmer"
person["age"] = 26

print(person)
for key in person:
    print(key, ":", person[key])

for key, value in person.items():
    print(f"{key} -> {value}")


sara = {
    "name" : "Sara",
    "age" : 29,
    "city" : "Boston",
    "hobby": "bake",
    "hobbies": "baking"
}

print(sara["name"])
sara["age"] = 30
sara["unit"] = "cyber"




moshe = {
    "name" : "Moshe",
    "age" : 24,
    "city" : "Haifa",
    "unit" : "None"
}

ron = {
    "name" : "Ron",
    "age" : 24,
    "city" : "Jerusalem",
    "unit" : "Programming"
}

david = {
    "name" : "David",
    "age" : 27,
    "city" : "Bene Brak",
    "unit" : "cyber"
}

names = [moshe, ron, david]


for person in names:
    print(f"{person["name"]} from {person["city"]} is {person["age"]} years old and serves in {person["unit"]}")








