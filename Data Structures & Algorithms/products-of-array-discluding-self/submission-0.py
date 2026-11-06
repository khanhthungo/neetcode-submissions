class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix prod 
        # suffix prod 
        # but arr retains state. at any pt 
        # we only care abt prev prod <-cnst * prev el 
        preProd = 1 
        res = [1]*len(nums)
        
        for i in range(len(nums)):
            res[i] *= preProd 
            # after res so the later iteration get the prev val 
            preProd *= nums[i] 
        
        sufProd = 1 
        for i in range(len(nums) - 1, -1, -1): 
            res[i] *= sufProd 
            sufProd *= nums[i]
        
        return res