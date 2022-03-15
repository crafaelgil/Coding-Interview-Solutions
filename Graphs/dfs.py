def dfs(V, adj):
  dfs = []
  queue = []
  visited = [False] * (V+1)

  for i in range(V+1):
    if len(adj[i]) > 0 and visited[adj[i]] == False:
      dfs_util(queue, visited, i, adj)

  return dfs

def dfs_util(queue, visited, i, adj):
  queue.append(i)
  visited[i] = True

  for node in adj[i]:
    if visited[i] == False:
      dfs_util(queue, visited, node, adj)

  return queue
