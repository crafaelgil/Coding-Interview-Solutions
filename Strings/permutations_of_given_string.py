class Solution:
  def __init__(self, a):
    self.a = a

  def permute(self, a, left, right):
    if left == right:
      print(''.join(a))

    else:
      for i in range(left, right+1):
        a[left], a[i] = a[i], a[left]
        self.permute(a, left + 1, right)
        a[left], a[i] = a[i], a[left]

  def find_permutations(self):
    a = list(str)
    return self.permute(a, 0, len(a) - 1)

str = "ABC"
solution = Solution(str)

print(solution.find_permutations())
