def find_sum_even_nums(nums, queries):
  sums = []

  for querie in queries:
    val, index = querie
    nums[index] += val

    sum = 0

    for num in nums:
      if num % 2 == 0:
        sum+=num

    sums.append(sum)

  return sums

nums = [1,2,3,4]
queries = [[1,0], [-3,1], [-4,0], [2,3]]

print(find_sum_even_nums(nums, queries))
