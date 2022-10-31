class Solution:
    def findMin(self, nums) -> int:
        def bsearch(l, r):
            # case1) 원소가 1개거나, 구간 전체가 순서대로 정렬된 경우
            if l==r or nums[l]<nums[r]:
                return nums[l]
            
            mid = l + (r-l)//2
            # case2-1) mid가 왼쪽 그룹 ascending order에 속하는 경우 
            # => 위에서 l이 가장 작을 경우가 걸려졌으므로, 오른쪽 그룹에서 찾는다
            if nums[l] <= nums[mid]:
                return bsearch(mid+1, r)
            # case2-2) 꺽이는 포인트가 왼쪽 그룹에 있었다는 뜻이므로, 왼쪽 그룹에서 찾는다.
            else:
                return bsearch(l, mid)
        
        l, r = 0, len(nums)-1
        return bsearch(l, r)