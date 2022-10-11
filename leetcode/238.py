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


# extra memory 사용 안하는 버전
# -> 방향 <- 방향으로 한번씩 순회하면서 최종 array 에 multiply
class Solution:
    def productExceptSelf(self, nums):
        result = []
        pre = 1
        
        for x in nums:
            result.append(pre)
            pre*=x
        
        length=len(nums)
        post = 1
        for i, x in enumerate(nums[::-1]):
            result[length-1-i]*=post
            post*=x
            
        return result