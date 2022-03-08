def find_equilibrium_point(arr):
  if not arr or len(arr) == 0:
    return []

  beg, end = 0, len(arr)-1

  sum_beg = arr[beg]
  sum_end = arr[end]

  while beg + 1 < end:
    if sum_beg < sum_end:
      beg+=1
      sum_beg += arr[beg]
    elif sum_beg > sum_end:
      end-=1
      sum_end += arr[end]
    else:
      return arr[beg + 1]

  return -1

# arr = [1,3,5,2,2]
arr = [1,2,3,4,5,10]

print(find_equilibrium_point(arr))
