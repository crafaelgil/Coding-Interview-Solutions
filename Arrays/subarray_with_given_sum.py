from numpy import array


class Solution():
  def __init__(self, arr, sum):
    self.arr = arr
    self.sum = sum

  def find_subarray(self):
    current_sum = arr[0]
    start = 0
    end = 1
    while end <= len(arr):
      while current_sum > sum and start < end - 1:
        current_sum-= arr[start]
        start+=1
      if current_sum == sum:
        return arr[start: end]
      if end < len(arr):
        current_sum+= arr[end]
        end+=1

  # def find_subarray(self):
  #   n = len(arr)
  #   for i in range(n):
  #     current_sum = arr[i]
  #     j = i + 1
  #     while j <= n:
  #       if current_sum == sum:
  #         return [i, j - 1]
  #       if current_sum > sum or j == n:
  #         break
  #       current_sum += arr[j]
  #       j+=1
  #   return []

arr = [15, 2, 4, 8, 9, 5, 10, 23]
sum = 23

solution = Solution(arr,sum)

print(solution.find_subarray())


