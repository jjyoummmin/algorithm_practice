# two pointer approach
class Solution:
    def maxArea(self, height):
        max_area = 0
        left, right = 0, len(height)-1
        
        while left < right:
            current = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current)
            
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return max_area