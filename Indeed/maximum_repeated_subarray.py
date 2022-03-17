def findLength(self, arr1: List[int], arr2: List[int]) -> int:
  if not arr1 or not arr2:
      return 0

  dp = [[1 for _ in range(len(arr2) + 1)] for _ in range(len(arr1) + 1)]

  for i in range(1, len(arr1)+1):
      for j in range(1, len(arr2)+1):
          if arr1[i-1] == arr2[j-1]:
              dp[i][j] = 1 + dp[i-1][j-1]
          else:
              dp[i][j] = max(dp[i][j-1], dp[i-1][j])

  return dp[len(arr1)-1][len(arr2)-1]
