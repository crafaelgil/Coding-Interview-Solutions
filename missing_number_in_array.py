from unittest import expectedFailure


class Solution:
  def __init__(self, arr):
    self.arr = arr

  def find_missing_number(self):
    a,b = 0, 0
    for i in range(len(arr)):
      a = a^arr[i]
    for i in range(1, len(arr)+2):
      b = b^i
    return a^b

    # arr.sort()
    # for i in range(len(arr)):
    #   if not arr[i] == i + 1:
    #     return i+1

    # n = len(arr)
    # expected_sum = int(n*(n+1)/2)
    # sum = 0
    # for i in range(n):
    #   sum+=arr[i]
    # return expected_sum - sum

arr = [6,1,2,8,3,4,7,10,5]
solution = Solution(arr)
print(solution.find_missing_number())
