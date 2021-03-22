#White spaces are not neccesarry => Can get rid of them
#Once I have the new string:
#Trivial yet super slow solution: Check every single permutation of the string -> Super slow O(len(newStr)!)
#There are two cases: the length of the string is even or odd
#Odd length palindromes can be split in two 'identical' halves aside form ordering of chars
#Each char in the left half must exist in the rigth half and viceversa
#Then if the length of newStr is even -> Check if every char has an even number of occurences
#This is enough since we can just take, for example abddcabc -> {a:2, b:2, c:2, d:2} -> Construct "abcddcba" -> Output true
#Second case is when the length of newStr is odd -> The MUST exist ONLY ONE single-coccurence char, the rest must have an even num of occurences
#Case 1: 0...len(newStr)/2
#Case 2: 0...floor(len(newStr+1))
#time: O(len(newStr))
#Space: O(len(newStr)) worst case "abcdbe"
#I don't think we can do better since we have to scan each char at least once
#Checking len of str is O(1)
#SOlution above is partially wrong
#We need ot check the whole string -> O(len(newStr)))

class Solution:
  def __init__(self, s):
    self.s = s

  def PalindromePermutation(self):
    newStr = self.s.replace(" ","").lower()
    strLength = len(newStr)
    charOcurrences = {}
    oddOcurrences = 0

    for c in newStr:
      if c in charOcurrences:
        charOcurrences[c] = (charOcurrences[c] + 1) % 2
      else:
        charOcurrences[c] = 1

    if strLength % 2: #odd
      for c in charOcurrences.keys():
        if oddOcurrences > 1:
          return False
        elif charOcurrences[c] == 1:
          oddOcurrences+=1
      return True
    else: #even
      for c in charOcurrences.keys():
        if charOcurrences[c] == 1:
          return False
      return True


string = "Tact Coa"
solution = Solution(string)
print(solution.PalindromePermutation())
