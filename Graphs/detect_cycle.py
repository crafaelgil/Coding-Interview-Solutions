from numpy import True_


def detect_cycle(V, adj):
  visited = [False] * V

  for u in range(V):
    if not visited[u]:
      if dfs(u, visited, -1, adj):
        return True

  return False

def dfs(u, visited, start, adj):
  visited[u] = True

  for v in adj[u]:
    if not visited[v]:
      if dfs(v,visited, u, adj):
        return True
    elif v != u:
      return True

  return False



