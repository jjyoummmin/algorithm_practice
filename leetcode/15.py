class Solution:
    sorted_nums = []
    rightmost = -1
    
    def twoSum(self, l, r, target):
        res_set = set()
        while l<r:
            x, y = self.sorted_nums[l], self.sorted_nums[r]
            if x+y == target:
                res_set.add((x,y))
                l+=1
                r-=1
            elif x+y < target:
                l+=1
            else: 
                r-=1
            
        return res_set
    
    def threeSum(self, nums):
        self.sorted_nums = sorted(nums)
        self.rightmost = len(nums)-1
        res = []
        seen = set()

        for i, val in enumerate(self.sorted_nums):
            if val >0:
                break
                
            if val in seen:
                continue
            
            seen.add(val)
            two_sum = self.twoSum(i+1, self.rightmost, -val)
            
            for tuple in two_sum:
              res.append([val, *tuple])
        
        return res