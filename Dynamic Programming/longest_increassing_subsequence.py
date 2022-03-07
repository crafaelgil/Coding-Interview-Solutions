def find_longest_subsequence(arr):
  if not arr:
    return 0

  L = [0] * len(arr)

  L[0] = 1

  for i in range(1, len(arr)):
    for j in range(i):
      if arr[j] < arr[i] and L[j] > L[i]:
        L[i] = L[j]
    L[i]+=1

  return max(L)

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(find_longest_subsequence(arr))
