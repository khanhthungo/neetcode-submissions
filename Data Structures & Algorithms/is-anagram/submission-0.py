class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(t)
        
        for i in range(len(s)): 
            if freq[s[i]] <= 0: 
                return False 
            freq[s[i]] -=1 
        
        return True if sum(freq.values()) == 0 else False