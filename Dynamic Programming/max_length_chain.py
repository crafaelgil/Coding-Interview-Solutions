def max_length_chain(pairs):
  pairs.sort(key=lambda x:x[0])

  dp = [1] * len(pairs)

  for i in range(len(pairs)):
    for j in reversed(range(i)):
      if pairs[j][1] < pairs[i][0]:
        dp[i] = dp[j] + 1
        break

  return max(dp)

pairs = [[1,2],[7,8],[4,5]]

print(max_length_chain(pairs))
