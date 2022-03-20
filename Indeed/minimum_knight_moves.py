import collections

def find_min_knight_moves(x,y):
  possible_moves = [
      (1, 2), (2, 1), (-1, 2),
      (-2, 1), (-1, -2), (-2, -1),
      (1, -2), (2, -1)
  ]

  que = collections.deque([[0, 0, 0]])
  visited = set()
  visited.add((0, 0))
  while que:
      qx, qy, d = que.popleft()
      if x == qx and y == qy:
          return d
      for dx, dy in possible_moves:
          nx, ny = qx + dx, qy + dy
          if (nx, ny) not in visited and nx >=-2 and ny>=-2:
              visited.add((nx, ny))
              que.append([nx, ny, d + 1])

print(find_min_knight_moves(2,1))
