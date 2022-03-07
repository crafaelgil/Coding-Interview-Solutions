def find_longest_bitonic_subsequence(arr):
  if not arr or len(arr) == 0:
    return 0

  I = [0] * len(arr) #ending at arr[i]
  D = [0] * len(arr) #starting at arr[i]

  I[0] = 1
  D[len(arr)-1] = 1

  for i in range(1, len(arr)):
    for j in range(i):
      if arr[j] < arr[i] and I[j] > I[i]:
        I[i] = I[j]
    I[i]+=1

  for i in reversed(range(len(arr)-1)):
    for j in reversed(range(i+1, len(arr))):
      if arr[j] < arr[i] and D[j] > D[i]:
        D[i] = D[j]
    D[i]+=1

  lbs_len = 1

  for i in range(len(arr)):
    lbs_len = max(lbs_len, I[i] + D[i] - 1)

  return lbs_len

arr = [4, 2, 5, 9, 7, 6, 10, 3, 1]
print(find_longest_bitonic_subsequence(arr))
