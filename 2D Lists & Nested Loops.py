# 2D Lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[1][2])

# nested for loop - to access all the items in the number_grid list
for row in number_grid:
    for column in row:
        print(column)
