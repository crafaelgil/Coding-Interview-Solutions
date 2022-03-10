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
        return coordinates

grid = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1]
]

print(find_rectangles(grid))
