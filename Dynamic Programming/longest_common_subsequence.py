def find_longest_common_subsequence(X,Y):
  table = [[0 for i in range(len(Y)+1)] for j in range(len(X)+1)]

  for i in range(1,len(X)+1):
    for j in range(1,len(Y)+1):
      if  X[i-1] == Y[j-1]:
        table[i][j] = 1 + table[i-1][j-1]
      else:
        table[i][j] = max(table[i][j-1], table[i-1][j])

  return table[len(X)-1][len(Y)-1]

X = "ACADB"
Y = "CBDA"

print(find_longest_common_subsequence(X,Y))
