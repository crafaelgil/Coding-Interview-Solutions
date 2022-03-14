from collections import defaultdict
import heapq as hp

def find_top_k_frequent_elements(nums, k):
  freq = defaultdict(int)

  for num in nums:
      if num not in freq.keys():
          freq[num] = -1
      else:
          freq[num] -= 1

  min_heap = []

  for key, value in freq.items():
      min_heap.append([value, key])

  hp.heapify(min_heap)

  top_k_freq_elem = []

  for i in range(k):
      freq, ele = hp.heappop(min_heap)
      top_k_freq_elem.append(ele)

  return top_k_freq_elem
