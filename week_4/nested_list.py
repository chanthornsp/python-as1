# Nested loops with a list of lists
matrix = [[1, 2, 3,10], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    # print(type(row))
    for number in row:
        print(number)