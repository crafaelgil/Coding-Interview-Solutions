from pickle import TRUE


class Solution:
  def __init__(self, arr):
    self.arr = arr

  def rearrange_array(self):
    new_arr = [None] * len(arr)
    small, large = 0, len(arr) - 1
    flag = True #true: copy large, false: copy small

    for i in range(len(arr)):
      if flag:
        new_arr[i] = arr[large]
        large-=1
      else:
        new_arr[i] = arr[small]
        small+=1
      flag = bool(1 - flag)

    return new_arr


arr = [1,2,3,4,5,6]
solution = Solution(arr)

print(solution.rearrange_array())
