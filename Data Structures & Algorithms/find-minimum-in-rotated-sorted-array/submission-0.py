class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) -1 
        res = float('inf')
        while l <= r: 
            m = l + (r-l)//2 
            if nums[m] >= nums[l] and nums[m] <= nums[r]: 
                return nums[l]
            elif nums[m] >= nums[l]: 
                l = m + 1 
            elif nums[m] <=nums[r]: 
                r = m 