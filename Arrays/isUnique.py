#s='abcdghaksu' -> False
#s='abcd' -> True
#if numChars is known => O(len(s)) sol: if len(s) > numChars => Pigenhole Principle -> False
#Hash Map -> {char: numOcurrences} -> We scan the string s -> O(len(s)) and check if char is in the hashmap
#Otherwise we store it -> O(1) to check in hashmap

class Solution:
  def __init__(self, s, numChars):
    self.s = s 
    self.numChars = numChars

  def isUnique(self):
    if len(s) > numChars:
      return False
    else:
      scannedChars = {}
      for c in s:
        if c in scannedChars:
          return False
        else:
          scannedChars[c] = 1
      return True

s = "abcdhfgksa"
numChars = 28
sol = Solution(s,numChars)
print(sol.isUnique())