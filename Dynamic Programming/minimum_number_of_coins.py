def min_num_coins(coins, amount):
  dp = [amount + 1] * (amount + 1)

  dp[0] = 0

  for a in range(1, amount+1):
    for c in coins:
      if a - c >= 0:
        dp[a] = min(dp[a], 1 + dp[a-c])

  return dp[amount]

coins = [1,2,3,4]
amount = 9

print(min_num_coins(coins, amount))


