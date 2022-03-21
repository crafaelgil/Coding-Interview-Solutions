def find_rectangle_with_max_area(grid):
  if not grid or len(grid) == 0:
    return

  num_rows = len(grid)
  num_cols = len(grid[0])

  hist = [0] * num_cols

  max_area = 0

  for row in range(num_rows):
    for col in range(num_cols):
      if grid[row][col] == 1:
        hist[col] += grid[row][col]
      else:
        hist[col] = 0

    max_area = max(max_area, find_largest_rectangle_in_histogram(hist))

  return max_area

def find_largest_rectangle_in_histogram(hist):
  stack = [] #(index, height)
  max_area = 0

  for i in range(len(hist)):
    start = i
    while stack and stack[-1][1] > hist[i]:
      index, height = stack.pop()
      max_area = max(max_area, height * (i - index))
      start = index
    stack.append((start, hist[i]))

  for index, height in stack:
    max_area = max(max_area, height * (len(hist) - index))

  return max_area

grid = [
  [1,0,1,0,0],
  [1,0,1,1,1],
  [1,1,1,1,1],
  [1,0,0,1,0]
]

print(find_rectangle_with_max_area(grid))
