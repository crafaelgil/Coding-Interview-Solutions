from pickle import TRUE

from numpy import True_


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

  num_calls = 0

  for row in range(num_rows):
    for col in range(num_cols):
      num_calls+=1
      new_rectangle_coordinates = []

      if grid[row][col] == 0:
        top_left_coordinate = [col, row]
        new_rectangle_coordinates.append(top_left_coordinate)

        #Find lower right coordinate
        while col + 1 < num_cols and grid[row][col+1] == 0:
          num_calls+=1
          col += 1
        while row + 1 < num_rows and grid[row+1][col] == 0:
          num_calls+=1
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
            num_calls+=1
            grid[row][col] = 1

        #Update row and col values to resume lookup
        row = top_left_coordinate[1]
        col = lower_right_coordinate[0]
  print(num_calls)
  return cooordinates

def find_multiple_rectangles_faster(grid):
  if not grid or len(grid) == 0:
    return []

  num_rows = len(grid)
  num_cols = len(grid[0])

  coordinates = []
  is_inside_rectangle_already_counted = False

  num_calls = 0

  for row in range(num_rows):
    for col in range(num_cols):
      num_calls+=1
      new_rectangle_coordinates = []

      if grid[row][col] == 0:
        #Check weather cell belongs to a rectangle previously counted
        for rectangle_coordinate in coordinates:
          if len(rectangle_coordinate) == 2:
            top_left = rectangle_coordinate[0]
            bottom_right = rectangle_coordinate[1]

            if top_left[1] <= row <= bottom_right[1] and top_left[0] <= col <= bottom_right[0]:
              is_inside_rectangle_already_counted = True
            else:
              is_inside_rectangle_already_counted = False
          elif rectangle_coordinate == [col, row]:
            is_inside_rectangle_already_counted = True
          else:
            is_inside_rectangle_already_counted = False
        #Update answer
        if not is_inside_rectangle_already_counted:
          top_left_coordinate = [col, row]
          new_rectangle_coordinates.append(top_left_coordinate)

          while col + 1 < num_cols and grid[row][col+1] == 0:
            num_calls+=1
            col += 1
          while row + 1 < num_rows and grid[row+1][col] == 0:
            num_calls+=1
            row += 1

          bottom_right_coordinate = [col, row]
          new_rectangle_coordinates.append(bottom_right_coordinate)

          if top_left_coordinate == bottom_right_coordinate:
            new_rectangle_coordinates.pop()

          coordinates.append(new_rectangle_coordinates)

  print(num_calls)
  return coordinates

grid = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1],
  [0,1,1,0,0]
]

# print(find_rectangles(grid))

print(find_multiple_rectangles(grid))

print(find_multiple_rectangles_faster(grid))
