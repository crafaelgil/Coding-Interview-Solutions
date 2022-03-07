def length_longest_common_substring(X,Y):
  lenX, lenY = len(X), len(Y)

  table = [[0 for _ in range(lenY + 1)] for _ in range(lenX + 1)]

  for i in range(1, lenX+1):
    for j in range(1, lenY + 1):
      if X[i-1] == Y[j-1]:
        table[i][j] = table[i-1][j-1] + 1
      else:
        table[i][j] = max(table[i-1][j], table[i][j-1])

  return table[lenX][lenY]

def find_shortest_supersequence(X,Y):
  return len(X) + len(Y) - length_longest_common_substring(X,Y)

str1 = "AGGTAB"
str2 = "GXTXAYB"

print(find_shortest_supersequence(str1, str2))
