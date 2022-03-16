def summaryRanges(self, nums: List[int]) -> List[str]:
  ranges = []
  i = 0

  while i < len(nums):
      start = i
      while i+1 < len(nums) and nums[i] + 1 == nums[i+1]:
          i+=1
      if start != i:
          ranges.append('{}->{}'.format(nums[start], nums[i]))
      else:
          ranges.append(str(nums[i]))
      i+=1

  return ranges
