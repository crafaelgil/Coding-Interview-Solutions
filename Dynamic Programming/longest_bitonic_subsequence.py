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

def print_longest_bitonic_subsequence(arr):
  num_ele = len(arr)

  if not arr or num_ele == 0:
    return []

  I = [[] for _ in range(num_ele)]
  D = [[] for _ in range(num_ele)]

  I[0].append(arr[0])
  D[num_ele-1].append(arr[num_ele-1])

  for i in range(1, num_ele):
    for j in range(i):
      if arr[j] < arr[i] and len(I[j]) > len(I[i]):
        I[i] = I[j].copy()
    I[i].append(arr[i])

  for i in reversed(range(num_ele-1)):
    for j in reversed(range(i+1, num_ele)):
      if arr[j] < arr[i] and len(D[j]) > len(D[i]):
        D[i] = D[j].copy()
    D[i].insert(0, arr[i])

  peak = 0

  for i in range(num_ele):
    if len(I[i]) + len(D[i]) > len(I[peak]) + len(D[peak]):
      peak = i

  D[peak].pop(0)

  for d in D[peak]:
    I[peak].append(d)

  return I[peak]

arr = [4, 2, 5, 9, 7, 6, 10, 3, 1]
print(print_longest_bitonic_subsequence(arr))
