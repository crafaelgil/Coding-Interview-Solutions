from collections import deque

class Solution:
  def __init__(self):
    self.arr = arr

  def find_next_greater_elements(self, arr):
    if not arr:
      return

    result = [-1] * len(arr)

    stack = deque()

    for i in range(len(arr)):
      while stack and arr[stack[-1]] < arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()

      stack.append(i)

    return result

arr = [1,3,2,4]
solution = Solution()

print(solution.find_next_greater_elements(arr))
