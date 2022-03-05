def min_num_coins(C, V):
  if V == 0:
    return 0

  for c in C:
    if c <= V:
      min_coins = min(min_coins, 1 + min_num_coins(C, V - c))
  return min_coins

C = [25,10,5]
V = 30

print(min_num_coins(C,V))
