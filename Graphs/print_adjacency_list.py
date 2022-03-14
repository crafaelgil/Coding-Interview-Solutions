def print_graph(V, adj):
  path = []

  for i in range(V):
    path.append([i] + adj[i])

  return path
