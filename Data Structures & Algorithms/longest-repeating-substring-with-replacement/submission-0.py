class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # iterate reader
        # build freq
        # if curr window len - freq max > k then shrink l 
        # update the global max 
        # l is valid window stopper 
        # r is reader n checks against eq   
        # moves while eq is still small or true 
        # shrink l once it turns false 


        # l n r moves til window valid 
        # then update res 
        # reutrn result 
        res = 0 
        l = 0 
        r = 0 
        freq = defaultdict(int)
        while r < len(s): 
            freq[s[r]] +=1 
            if r - l + 1 - max(freq.values()) > k: 
                freq[s[l]] -=1 
                l +=1 
            res = max(res, r - l + 1)
            r +=1 

        return res 
                 

