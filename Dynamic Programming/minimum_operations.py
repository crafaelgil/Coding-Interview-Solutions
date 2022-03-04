from unittest import result


class Solution:
  def __init__(self):
    return

  def min_operation(self, n):
    if n < 0:
      return -1
    if n < 2:
      return n
    else:
      if n%2 == 0:
        result = 1 + self.min_operation(n//2)
      else:
        result = 1 + self.min_operation(n-1)
      return result

solution = Solution()

print(solution.min_operation(5))
