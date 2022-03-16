def find_number_of_islands_dfs(grid):
  def search_dfs(row, col, grid):
    if not (0 <= row < num_rows and 0 <= col < num_cols):
      return

    if grid[row][col] == 0:
      return

    grid[row][col] = 0

    search_dfs(row+1, col, grid)
    search_dfs(row-1, col, grid)
    search_dfs(row, col+1, grid)
    search_dfs(row, col-1, grid)


  if not grid:
    return

  num_islands = 0

  num_rows = len(grid)
  num_cols = len(grid[0])

  for row in range(num_rows):
    for col in range(num_cols):
      if grid[row][col] == 1:
        num_islands += 1
        search_dfs(row, col, grid)

  return num_islands

def find_number_of_islands_bfs(grid):
  if not grid:
    return

  num_islands = 0

  num_rows = len(grid)
  num_cols = len(grid[0])

  visited = set()

  def bfs(row, col):
    queue = [(row, col)]
    visited.add((row, col))

    directions = [[-1,0],[1,0],[0,1],[0,-1]]

    while len(queue):
      row, col = queue.pop(0)

      for drow, dcol in directions:
        r, c = row + drow, col + dcol
        if r in range(num_rows) and c in range(num_cols) and grid[r][c] == 1 and (r,c) not in visited:
          grid[r][c] = 0
          queue.append((r,c))
          visited.add((r,c))

  for row in range(num_rows):
    for col in range(num_cols):
      if grid[row][col] == 1 and (row,col) not in visited:
        bfs(row, col)
        num_islands += 1

  return num_islands

grid = [
  [1,1,1,0,0,1,1],
  [1,1,0,0,1,1,1],
  [0,1,0,0,0,1,0],
  [0,0,0,0,0,0,1]
]

# print(find_number_of_islands_dfs(grid))
print(find_number_of_islands_bfs(grid))
