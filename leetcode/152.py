class Solution:
  def maxProduct(self, nums) -> int:
    result = max(nums)
    prevMin, prevMax = 1, 1

    for n in nums:
      if n==0:
        prevMin, prevMax = 1, 1
        continue

      candidate = [prevMin*n, prevMax*n, n]
      prevMin = min(candidate)
      prevMax = max(candidate)
      result = max(result, prevMax)

    return result 
        