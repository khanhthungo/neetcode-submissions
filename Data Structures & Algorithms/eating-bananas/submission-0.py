class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort() 
        res = float('inf')
        l = 1 
        r = max(piles)

        while l <= r: 
            m = l + (r-l)//2 
            if self.bs(piles, m, h): 
                res = min(res, m)
                r = m - 1
            else: 
                l = m + 1
        
        return res
    
    def bs(self, piles, m, h): 
        t = 0 
        for i in range(len(piles)): 
            t += math.ceil(piles[i]/m)
        
        return True if t <= h else False 