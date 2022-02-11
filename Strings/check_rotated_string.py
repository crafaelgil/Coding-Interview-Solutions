class Solution:
  def __init__(self, str1, str2):
    self.str1 = str1
    self.str2 = str2

  def check_rotated_string(self):
    if (len(str1) != len(str2)):
        return False

    if(len(str1) < 2):
        return str1 == str2
    # clock_rot = ""
    # anticlock_rot = ""
    l = len(str2)

    # Initialize string as anti-clockwise rotation
    anticlock_rot =  str2[l - 2:] + str2[0: l - 2]

    # Initialize string as clock wise rotation
    clock_rot = str2[2:] + str2[0:2]

    # check if any of them is equal to string1
    return (str1 == clock_rot or str1 == anticlock_rot)

str1 = "fsbcnuvqhffbsaqxwp"
str2 = "wpfsbcnuvqhffbsaqx"
# str1 = "amazon" #on amaz  azon am
# str2 = "azonam" #azon am

solution = Solution(str1, str2)
print(solution.check_rotated_string())
