#First ideaL check every char in str and replace blanck space with %20
#str = 'a b c d         '
#str = 'aba  jsbs j s                '
#Need to shift next chars to the rigth -> O(numBlankSpaces * numChars) = O(numBlankSpaces * (len(str) - numBlankSpaces))
#At the end of the string there is 3k number of white spaces where k is the number of blanck spaces in the 'original string'
#When I see a blanck space I copy the next two elements of the string to the end of the array, then subsitute ' ' with '%20'
#Array lookup takes O(1) because of some python implementation
#str = 'ab cd e      '
#str = 'ab%20cd e  cd'
#A bit difficult to implement
#Other solution requires an extra array. Just copy each element from str to arr and when see a white space just write '%20' and then keep copyng chars
#O(len(str)) time but O(len(str)) space
#On average it is more likely to have numChars > numBlanckSpaces => O(numChars^2) -> Slow
#Note that python strings are inmutable => Convert string to list

class Solution:
  def __init__(self,s):
    self.s = s

  def URLify(self):
    strLen = len(self.s.strip())
    charList = list(self.s)
    placeIndex = len(self.s)

    for i in range(strLen, 0, -1):
      if charList[i] == " ":
        charList[placeIndex - 3 : placeIndex] = "%20"
        placeIndex-=3
      else:
        charList[placeIndex - 1] = charList[i]
        placeIndex-=1

    return ''.join(charList)

testString = "a b c d         "
solution = Solution(testString)
print(solution.URLify())
