def transitive_closure( N, graph):
  for i in range(N):
      graph[i][i] = 1


  for t in range(N):
      for i in range(N):
          for j in range(N):
              if graph[i][t] == 1 and graph[t][j] == 1:
                  graph[i][j] = 1
  return graph
