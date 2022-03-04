import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"


# pip install clipboard - is required

data = clipboard.paste()  # read the data from the clipboard
# print(data)

# access the different command line arguemnts
print(sys.argv)

# we want to exclude the first argument which is our file name - we use slicing
# print(sys.argv[1:])

# we create a json file or overwrite it if the file already exists, and we open it in write mode with the "w"


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# save_items("test.json", {"key": "value"})
def load_json_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


# we want only one command after our file name
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_json_items(SAVED_DATA)
    print(command)
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("data saved!")

    if command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else:
            print("Key does not exist")
    if command == "list":
        print(data)
    else:
        print("unknown command")
else:
    print("Please pass exactly one command")
