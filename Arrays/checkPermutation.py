#Permutation: Rearrangement of elements
#If they have the same chars then one is a permutation of the other
#str1, str2
#check len(str1) == len(str2) ? Possible ? False -> O(1)
#Scan all chars of str1 and store them in hashmap1 -> O(len(str1))
#Scan all chars of str2 and store them in hashmap2 -> O(len(str2))
#For every key in hashmap1 check if value is the same as in hashmap2 (if exists -> O(1) for lookup -> O(len(hashmap1.keys))
#If for every key in hashmap1 has the same value as in hashmap2 => True oherwise False
#len(hashmap1.keys) has to be equal to len(hasmap2.keys)
#O(1 + len(str1) + len(str2) + len(hashmap1.keys or hashmap2.keys))
#len(str1 or str2) >= len(hashmap1.keys or hashmap2.keys)
#O(len(str1 or str2))

class Solution:
  def __init__(self, str1, str2):
    self.str1 = str1
    self.str2 = str2

  def checkPermutation(self):
    if not len(self.str1) == len(self.str2):
      return False
    else:
      hashmap1 = {}
      hashmap2 = {}

      for c in self.str1:
        if c not in hashmap1:
          hashmap1[c] = 1
        else:
          hashmap1[c]+=1
      for c in self.str2:
        if c not in hashmap2:
          hashmap2[c] = 1
        else:
          hashmap2[c]+=1

      for c in hashmap1:
        if c in hashmap2:
          if not hashmap1[c] == hashmap2[c]:
            return False
        else:
          return False
      return True

str1 = 'abcdef'
str2 = 'abfdee'
solution = Solution(str1, str2)
print(solution.checkPermutation())

