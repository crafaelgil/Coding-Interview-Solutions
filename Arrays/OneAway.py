#First idea: One edit away -> They differ in at last one char
#str1, str2 => if abs(len(str1) - len(str2)) <= 1 ? possible : False
#Three cases: len(str1) > len(str2), len(str2) > len(str1), len(str1) = len(str2)
#If lengths are different then we cnvert each string into a list and then check wether one list is contained in the other
#abcdefgh
#abcdfgh

class Solution:
  def __init__(self, str1, str2):
    self.str1 = str1
    self.str2 = str2
  
  def OneAway(self):
    len1 = len(str1)
    len2 = len(str2)

    list1 = list(str1)
    list2 = list(str2)

    if abs(len1 - len2) > 1 :
      return False
    elif len1 == len2: #Replace
      numDiffChars = 0
      for i in range(len1):
        if numDiffChars > 1:
          return False
        if not list1[i] == list2[i]:
          numDiffChars+=1
      return True
    elif len1 == 1 + len2: 
      return self.checkOneAway(list2, list1)
    else:
      return self.checkOneAway(list1, list2)
  
  def checkOneAway(self, list1, list2): #len1 < len2
    i = 0
    numDiffChars = 0
    for element in list1:
      if numDiffChars > 1:
        return False
      if not element == list2[i]:
        numDiffChars+=1
        i+=1
      i+=1
    return True
      

str1 = "pales"
str2 = "bake"
solution = Solution(str1, str2)
print(solution.OneAway())