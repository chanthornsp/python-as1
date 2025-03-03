import json
file_name = 'data.json'
try:
    with open(file_name,mode='r') as file:
        data = json.load(file)
        print(data)
except PermissionError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except json.JSONDecodeError as e:
    print(e)

# write to json file

data = {
    'name':'John',
    'age':25,
    'city':'New York'
}
try:
    with open(file_name,mode='w') as file:
        json.dump(data,file,indent=2)
except PermissionError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except json.JSONDecodeError as e:
    print(e)