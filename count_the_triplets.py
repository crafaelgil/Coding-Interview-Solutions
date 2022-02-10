class Solution:
  def __init__(self, arr):
    self.arr = arr

  def find_triplets(self):
    set_nums = set(arr)
    count = 0
    for i in range(len(arr)):
      for j in range(i+1, len(arr)):
        if arr[i] + arr[j] in set_nums:
          count+=1
    return count


arr = [2,3,4]
solution = Solution(arr)
print(solution.find_triplets())
