try:
    with open('not.txt') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print("File ot found!!!")