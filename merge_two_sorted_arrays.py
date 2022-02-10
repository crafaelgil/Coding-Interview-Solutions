class Solution:
  def __init__(self, arr1, arr2):
    self.arr1 = arr1
    self.arr2 = arr2

  def merge_arrays(self):
    i,j,k = 0,0,len(arr1) - 1

    while i <= k and j < len(arr2):
      if arr1[i] < arr2[j]:
        i+=1
      else:
        temp = arr2[j]
        arr2[j] = arr1[k]
        arr1[k] = temp
        j+=1
        k-=1

    arr1.sort()
    arr2.sort()

    return [arr1, arr2]

arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

solution = Solution(arr1, arr2)
print(solution.merge_arrays())
