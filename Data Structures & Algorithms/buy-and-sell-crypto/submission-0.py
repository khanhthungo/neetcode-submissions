class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through the array 
        # l keeps track of lowest 
        # r exhausts -> r ? l 
        # < thi update l 
        # > thi check against global 

        maxP = 0 
        l = 0 
        r = l + 1 
        while r < len(prices): 
            if prices[r] < prices[l]: 
                l = r 
            else: 
                p = prices[r] - prices[l]
                maxP = max(p, maxP)
            r +=1 
        
        return maxP