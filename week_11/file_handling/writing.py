file_name = 'sample_write.txt'
try:
    with open(file_name,'w') as file_write:
        file_write.write('This is a sample text file.\n')
        file_write.write('This is the second line of the file.\n')
except PermissionError as e:
    print(f'Permission denied to open file named sample_write.txt. Error: {e}')

try:
    with open(file_name,'a') as file_append:
        file_append.write('This is the third line of the file.\n')
except PermissionError as e:
    print(f'Permission denied to open file named sample_write.txt. Error: {e}')