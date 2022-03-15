def find_number_of_provinces(V, adj):
  num_provinces = 0

  for i in range(V+1):
    bfs(V, i, adj)
    num_provinces += 1

  return num_provinces

def bfs(V, starting_node, adj):
  queue = [starting_node]
  visited = [False] * (V+1)

  while len(queue) > 0:
    u = queue.pop(0)

    for v in adj[u]:
      if visited[v] == False:
        queue.append(v)
        visited[v] = True
