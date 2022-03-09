def find_max_len_of_repeated_subarray(arr1, arr2):
  if not(arr1 and arr2) or len(arr1)+len(arr2) == 0:
    return 0

  dp = [[1 for _ in range(len(arr2) + 1)] for _ in range(len(arr1) + 1)]

  for i in range(1, len(arr1)+1):
    for j in range(1, len(arr2)+1):
      if arr1[i-1] == arr2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])

  return dp[len(arr1)-1][len(arr2)-1]

# arr1 = [1,2,3,2,1]
# arr2 = [3,2,1,4,7]
arr1 = [0,0,0,0,0]
arr2 = [0,0,0,0,0]

print(find_max_len_of_repeated_subarray(arr1, arr2))
