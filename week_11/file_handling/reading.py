filename = 'output.txt'
try:
    with open(filename) as file_read:
        content = file_read.read()
        print(content)
except FileNotFoundError as e:
    print(f'File named {filename} not found. Error: {e}')
except PermissionError as e:
    print(f'Permission denied to open file named {filename}. Error: {e}')
