def longest_palindromic_subsequence(seq, i, j):
  if i == j:
    return 1

  if seq[i] == seq[j] and j == i+1:
    return 2

  if seq[i] == seq[j]:
    return longest_palindromic_subsequence(seq, i+1, j-1) + 2

  return max(longest_palindromic_subsequence(seq, i+1, j), longest_palindromic_subsequence(seq, i, j-1))

def dp_solution(seq):
  n = len(seq)

  table = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    table[i][i] = 1

  for cl in range(2, n+1):
    for i in range(n - cl + 1):
      j = i + cl - 1
      if seq[i] == seq[j] and cl == 2:
        table[i][j] = 2
      elif seq[i] == seq[j]:
        table[i][j] = table[i+1][j-1] + 2
      else:
        table[i][j] = max(table[i+1][j], table[i][j-1])

  return table[0][n-1]

seq = "GEEKSFORGEEKS"
print(longest_palindromic_subsequence(seq, 0, len(seq)-1))
print(dp_solution(seq))
