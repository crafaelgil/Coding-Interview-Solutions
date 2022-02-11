from re import S


class Solution:
  def __init__(self, S):
    self.S = S

  def remove_duplicates(self, st):
    n = len(st)

    if n < 2:
      return st
    if st[0] == st[1]:
      return self.remove_duplicates(st[1:])
    else:
      return st[0] + self.remove_duplicates(st[1:])

S = "geeksforgeek"
solution = Solution(S)
print(solution.remove_duplicates(S))
