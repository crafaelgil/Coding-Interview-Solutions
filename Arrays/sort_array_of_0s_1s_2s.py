def sort_array(arr):
  if not arr or len(arr) == 0:
    return []

  zeros = ones = twos = 0

  for a in arr:
    if a == 0:
      zeros+=1
    elif a == 1:
      ones += 1
    else:
      twos += 1

  for i in range(zeros):
    arr[i] = 0
  for i in range(zeros, zeros + ones):
    arr[i] = 1
  for i in range(zeros + ones, len(arr)):
    arr[i] = 2

  return arr

arr = [0,2,1,2,0]

print(sort_array(arr))
