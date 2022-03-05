def longest_repeating_subsequence(seq):
  n = len(seq)

  table = [[0 for _ in range(n+1)] for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, n+1):
      if seq[i-1] == seq[j-1] and i != j:
        table[i][j] = table[i-1][j-1] + 1
      else:
        table[i][j] = max(table[i-1][j], table[i][j-1])

  return table[n-1][n-1]

seq = "aab"
print(longest_repeating_subsequence(seq))
