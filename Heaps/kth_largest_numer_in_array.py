from audioop import reverse
import heapq as hp

def find_kth_largest_element(nums, k):
  if not nums:
    return

  for i in range(len(nums)):
    nums[i] = -1 * nums[i]

  hp.heapify(nums)

  for i in range(k-1):
    hp.heappop(nums)

  return nums[0]

def simpler_solution(nums, k):
  nums.sort(reverse=True)

  return nums[k-1]
