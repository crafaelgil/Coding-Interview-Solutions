class Solution:
    def dfs(self, i, adj, visited, onpath):
        if visited[i]:
            return False
        visited[i] = True
        onpath[i] = True
        for ne in adj[i]:
            if onpath[ne]:
                return True
            if self.dfs(ne, adj, visited, onpath):
                return True
        onpath[i] = False
        return False


    def isPossible(self,N,prerequisites):
        adj = [[] for _ in range(N)]
        for v, u in prerequisites:
            adj[u].append(v)

        visited = [False] * N
        onpath = [False] * N

        for i in range(N):
            if not visited[i]:
                if self.dfs(i, adj, visited, onpath):
                    return False
        return True
