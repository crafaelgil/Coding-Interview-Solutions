def find_number_of_islands(grid):
  def search(row, col, grid):
    if not (0 <= row < num_rows and 0 <= col < num_cols):
      return

    if grid[row][col] == 0:
      return

    grid[row][col] = 0

    search(row+1, col, grid)
    search(row-1, col, grid)
    search(row, col+1, grid)
    search(row, col-1, grid)


  if not grid:
    return

  num_islands = 0

  num_rows = len(grid)
  num_cols = len(grid[0])

  for row in range(num_rows):
    for col in range(num_cols):
      if grid[row][col] == 1:
        num_islands += 1
        search(row, col, grid)

  return num_islands

grid = [
  [1,1,1,0,0,1,1],
  [1,1,0,0,1,1,1],
  [0,1,0,0,0,1,0],
  [0,0,0,0,0,0,1]
]

print(find_number_of_islands(grid))
