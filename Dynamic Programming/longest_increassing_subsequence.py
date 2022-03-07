from numpy import append


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

arr = [2, 6, 3, 4, 1, 2, 9, 5, 8]
print(find_longest_subsequence(arr))


def non_dp_solution(arr):
  if not arr:
    return 0

  S = [arr[0]]

  for i in range(1, len(arr)):
    if arr[i] > S[-1]:
      S.append(arr[i])
    else:
      smallest_larger = find_smallest_larger(S,arr[i])
      S[smallest_larger] = arr[i]

  return len(S)


def find_smallest_larger(S, a):
  l, r = 0, len(S)-1

  while l + 1 < r:
    m = (l+r)//2

    if a <= S[m]:
      r = m
    else:
      l = m

  return r

print(non_dp_solution(arr))

