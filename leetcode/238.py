class Solution:
    def productExceptSelf(self, nums):
        def cumulativeProd(arr):
            result = [1]
            prod = 1
            for x in arr:
                prod *= x
                result.append(prod)
            return result
        
        prod_left = cumulativeProd(nums)
        prod_right = cumulativeProd(nums[::-1])
        
        length = len(nums)
        result = [prod_left[i] * prod_right[length-i-1] for i in range(length)]
        return result