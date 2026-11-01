class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        missing = len(t)
        res = [float('inf'), 0]
        l = 0 

        for r, c in enumerate(s): 
            if freq[c] > 0: 
                missing -=1 
            freq[c] -=1 

            while missing ==0: 
                res = min(res, [r-l +1, l])
                if freq[s[l]] == 0: 
                    missing +=1 
                freq[s[l]] +=1 
                l+=1 
        return "" if res[0] == float('inf') else s[res[1]: res[1] + res[0]]