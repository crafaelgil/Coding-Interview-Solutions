def find_longest_common_substring(X,Y):
  table = [[0 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]

  result = 0

  for i in range(1, len(X)+1):
    for j in range(1,len(Y)+1):
      if X[i-1] == Y[j-1]:
        table[i][j] = table[i-1][j-1] + 1
        result = max(result, table[i][j])

  return result

X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'

print(find_longest_common_substring(X,Y))
