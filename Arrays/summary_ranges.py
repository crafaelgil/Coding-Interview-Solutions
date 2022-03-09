def find_summary_ranges(nums):
  if not nums or len(nums) == 0:
    return []

  ans = []
  i = 0

  while i < len(nums):
    start = i
    while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
      i+=1
    if start != i:
      ans.append('{}->{}'.format(nums[start], nums[i]))
    else:
      ans.append(str(nums[start]))
    i+=1

  return ans

nums = [0,1,2,4,5,7]
print(find_summary_ranges(nums))
