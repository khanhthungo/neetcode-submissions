class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0 
        for s in seen: 
            if s-1 not in seen: 
                seq = 1
                while s+1 in seen: 
                    seq +=1 
                    s +=1 
                res = max(res, seq)
        
        return res