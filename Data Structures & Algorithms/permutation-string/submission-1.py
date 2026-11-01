class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        l = 0 
        missing = len(s1)

        for r, c in enumerate(s2): 
            if freq[c] > 0: 
                missing -=1
            freq[c] -=1 

            while missing == 0: 
                if r - l + 1 == len(s1): 
                    return True 
                if freq[s2[l]] == 0: 
                    missing +=1
                freq[s2[l]] +=1 
                l +=1
        return False
                