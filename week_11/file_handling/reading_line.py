file = 'sample_write.txt'
try:
    with open(file,'r') as file:
        # line_content = file.readline()
        # print(line_content)
        lines = file.readlines()
        for index,value in enumerate(lines,1):
            print(f'Line: {index} - {value}')
except PermissionError as e:
    print(e)

