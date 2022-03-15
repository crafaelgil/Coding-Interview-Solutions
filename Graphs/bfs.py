def bfsOfGraph(V, adj):
  visited = [False] * (V+1)
  queue = [0]
  bfs = []

  while len(queue) > 0:
      current_node = queue.pop(0)
      bfs.append(current_node)

      for node in adj[current_node]:
          if visited[node] == False:
              visited[node] = True
              queue.append(node)

  return bfs
