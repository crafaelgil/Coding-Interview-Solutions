def find_longest_bitonic_subarray(arr):
  if not arr or len(arr) == 0:
    return 0

  I = [1] * len(arr)
  D = [1] * len(arr)

  for i in range(1, len(arr)):
    if arr[i-1] < arr[i]:
      I[i] = I[i-1] + 1

  for i in reversed(range(len(arr)-1)):
    if arr[i] > arr[i+1]:
      D[i] = D[i+1] + 1

  lbs_len = 1
  start = end = 0

  for i in range(len(arr)):
    if lbs_len < I[i] + D[i] - 1:
      lbs_len = I[i] + D[i] - 1
      start = i - I[i] + 1
      end = i + D[i] - 1

  return arr[start: end+1]

arr = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
print(find_longest_bitonic_subarray(arr))
