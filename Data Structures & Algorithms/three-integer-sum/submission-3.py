class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()
        
        for i in range(len(nums)-2): 
            l = i+1
            r = len(nums) -1 

            while l < r: 
                tsum = nums[l] + nums[r] + nums[i]
                if tsum == 0: 
                    results.add((nums[i],nums[l],nums[r]))
                    l+=1 
                    r-=1 
                elif tsum < 0: 
                    l+=1 
                elif tsum > 0: 
                    r-=1
        return list(list(i) for i in results) 