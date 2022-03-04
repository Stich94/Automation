
for item in (1, 2, 3, 4):
    print(item)

user = {
    "name": "Golem",
    "age": 45,
    "can_swim": False
}

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value)

print(user["name"])
