def find_rectangles(grid):
  if not grid or len(grid) == 0:
    return []

  num_rows = len(grid)
  num_cols = len(grid[0])

  coordinates = []

  for row in range(num_rows):
    for col in range(num_cols):
      if grid[row][col] == 0:
        coordinates.append([row, col])
        while col + 1 < num_cols and grid[row][col+1] == 0:
          col += 1
        while row + 1 < num_rows and grid[row+1][col] == 0:
          row += 1
        coordinates.append([col, row])
        if coordinates[0] == coordinates[1]:
          coordinates.pop()
        return coordinates

def find_multiple_rectangles(grid):
  if not grid or len(grid) == 0:
    return []

  num_rows = len(grid)
  num_cols = len(grid[0])

  cooordinates = []


  for row in range(num_rows):
    for col in range(num_cols):
      new_rectangle_coordinates = []

      if grid[row][col] == 0:
        top_left_coordinate = [col, row]
        new_rectangle_coordinates.append(top_left_coordinate)

        #Find lower right coordinate
        while col + 1 < num_cols and grid[row][col+1] == 0:
          col += 1
        while row + 1 < num_rows and grid[row+1][col] == 0:
          row += 1

        #Update
        lower_right_coordinate = [col, row]
        new_rectangle_coordinates.append(lower_right_coordinate)

        #Handle case when the rectangle is just one cell
        if top_left_coordinate == lower_right_coordinate:
          new_rectangle_coordinates.pop()

        cooordinates.append(new_rectangle_coordinates)

        #Update cell value to avoid overcount
        for row in range(top_left_coordinate[1], lower_right_coordinate[1]+1):
          for col in range(top_left_coordinate[0], lower_right_coordinate[0]+1):
            grid[row][col] = 1

        #Update row and col values to resume lookup
        row = top_left_coordinate[1]
        col = lower_right_coordinate[0]

  return cooordinates


grid = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1],
  [0,1,1,0,0]
]

# print(find_rectangles(grid))

print(find_multiple_rectangles(grid))
