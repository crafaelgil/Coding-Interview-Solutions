from sys import maxsize

class Solution:
  def __init__(self, arr):
    self.arr = arr

  def find_max_subarray(self):
    max_sum = -maxsize-1
    sum = 0
    for i in range(len(arr)):
      sum+=arr[i]
      if max_sum < sum:
        max_sum = sum
      if sum < 0:
        sum = 0
    return max_sum

arr = [-4 -5 -5 -3]
solution = Solution(arr)
print(solution.find_max_subarray())
