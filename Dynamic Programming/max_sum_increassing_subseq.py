def find_max_sum_inc_subseq(arr):
  if not arr or len(arr) == 0:
    return 0

  max_sum = [0] * len(arr) #max_sum stores max sum where last ele is arr[i]

  max_sum[0] = arr[0]

  for i in range(1, len(arr)):
    for j in range(i):
      if arr[j] < arr[i] and max_sum[j] > max_sum[i]:
        max_sum[i] = max_sum[j]
    max_sum[i]+=arr[i]

  max_inc_sum = 0

  for i in range(len(arr)):
    max_inc_sum = max(max_inc_sum, max_sum[i])

  return max_inc_sum

arr = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
print(find_max_sum_inc_subseq(arr))
