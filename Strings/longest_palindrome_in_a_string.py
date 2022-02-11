class Solution:
  def __init__(self, str):
    self.str = str

  def find_longest_palindrome(self):
    res = ""
    res_len = 0
    n = len(str)
    for i in range(n):
      #odd
      l,r = i,i
      while l>=0 and r < n and str[l] == str[r]:
        if r-l+1 > res_len:
          res_len = r-l+1
          res = str[l:r+1]
        l-=1
        r+=1

      #even
      l,r = i,i+1
      while l>=0 and r < n and str[l] == str[r]:
        if r-l+1 > res_len:
          res_len = r-l+1
          res = str[l:r+1]
        l-=1
        r+=1

    return res

str = "aaaabbaa"
solution = Solution(str)

print(solution.find_longest_palindrome())
