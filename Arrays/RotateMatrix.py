#The most basic idea is to use an extra 2-dimensional array and simply copy each column of the original matrix into its correspondent row
#Super slow -> O(N^2)
#Try to find an inverse matrix (solve the equiation)
# (0,0) (0,1) (0,2)      (0,2) (1,2) (2,2)
# (1,0) (1,1) (1,2) ---> (0,1) (1,1) (2,1)
# (2,0) (2,1) (2,2)`     (0,0)`(1,0) (2,0)
#Coordinate (0,0) -> (0,2), (2,1) -> (1,0), 
#In general coordinate (i,j) -> (j,N-1-i)
#A rotation is the result of the composition of two reflections

class Solution:
  def __init__(self, matrix):
    self.matrix = matrix
  
  def printMatrix(self, matrix):
      for i in range(len(self.matrix)):
        print(self.matrix[i])

  def RotateMatrix(self):
    dimension = len(self.matrix)
    
    for i in range(dimension):
      for j in range(dimension):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

solution = Solution(matrix)
rotatedMatrix = solution.RotateMatrix()
solution.printMatrix(rotatedMatrix)