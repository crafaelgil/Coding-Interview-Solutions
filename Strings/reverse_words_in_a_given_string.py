class Solution:
  def __init__(self, str):
    self.str = str

  def reverse_string(self):
    temp = []
    index = 0

    for i in range(len(str)):
      if str[i] == '.':
        temp.append(str[index:i])
        i+=1
        index = i

    temp.append(str[index:])

    temp = temp[::-1]

    return '.'.join(temp)

# str = 'i.like.this.program.very.much'
str = 'this.is.just.a.test'
solution = Solution(str)

print(solution.reverse_string())
