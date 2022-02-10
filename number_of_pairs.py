from itertools import count
import math
from re import X
from tkinter import Y

class Solution:
  def __init__(self, X, Y):
    self.X = X
    self.Y = Y

  def find_pairs(self):
    num_pairs = 0

    X.sort(reverse=True)
    Y.sort(reverse=True)

    for i in range(len(X)):
      for j in range(len(Y)):
        if math.pow(X[i],Y[j]) > math.pow(Y[j],X[i]):
          num_pairs+= len(Y) - j
          break

    return num_pairs

X = [2,3,4,5]
Y = [1,2,3]

solution = Solution(X,Y)
print(solution.find_pairs())
