#Basic idea: Run througth the entire string and count the number of occurences of a particular char
#O(len(str)) solution. I do not think we can do better than this since we have to check every char of the string
#Strings are inmutable => need to conver to list
#Iterate over the list
#Create new hashmap

class Solution:
  def __init__(self, s):
    self.s = s

  def StringCompression(self):
    compressedStr = []
    counter = 0

    for i in range(len(self.s)):
      if i != 0 and not self.s[i] == self.s[i-1]:
        compressedStr.append(self.s[i-1] + str(counter))
        counter = 0
      counter+=1

    if counter:
      compressedStr.append(self.s[-1] + str(counter))

    return min(self.s, ''.join(compressedStr), key=len)

s = "aabcccccaaa"
solution = Solution(s)
print(solution.StringCompression())
