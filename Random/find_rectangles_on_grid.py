def find_single_rectangle(grid):
  if not grid:
    return []

  num_cols = len(grid[0])
  num_rows = len(grid)

  ans = []

  for row in range(num_rows):
    for col in range(num_cols):
      if grid[row][col] == 0:
        ans.append([col, row])
        while row < num_rows and col < num_cols and grid[row+1][col+1] == 0:
          row += 1
          col += 1
        ans.append([col, row])
        return ans

  return []

def find_multiple_rectangles(grid):
  if not grid:
    return []

  num_cols = len(grid[0])
  num_rows = len(grid)

  rectangles = []




grid1 = [
  [1,1,1,1,1],
  [1,0,0,1,1],
  [1,0,0,1,1],
  [1,1,1,1,1]
]

grid2 = [
  [1,1,1,1,1],
  [1,0,0,1,1],
  [1,0,0,1,1],
  [1,1,1,1,0]
]

print(find_single_rectangle(grid1))
