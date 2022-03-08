import unittest

# class TestSum(unittest.TestCase):
#   def test_sum(self):
#     self.assertEqual(sum([1,2,3], 6, "Should be 6"))

#   def test_sum_2(self):
#     self.assertEqual(sum((1,2,3)), 6, "Should be 6")

# if __name__ == "__main__":
#   unittest.main()

from my_sum import sum

class TestSum(unittest.TestCase):
  def test_list_int(self):
    data = [1,2,3]
    result = sum(data)
    self.assertEqual(result, 6)

if __name__ == "__main__":
  unittest.main()
