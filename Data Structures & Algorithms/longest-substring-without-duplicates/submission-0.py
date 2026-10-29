class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0 
        l = 0 
        r = 0 
        seen = set()
        while r < len(s): 
            while s[r] in seen: 
                seen.remove(s[l])
                l +=1 

            seen.add(s[r])
            result = max(result, len(seen))
            r+=1 
        return result 