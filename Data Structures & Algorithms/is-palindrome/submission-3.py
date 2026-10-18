class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = s.lower()
        l = 0 
        r = len(s) -1 
        while l < r:
            while l < r and not self.isAlphaNum(ls[l]): 
                l+=1 
            while l < r and not self.isAlphaNum(ls[r]): 
                r-=1 
            if ls[l] != ls[r]: 
                return False
            l+=1 
            r-=1 
        return True

    def isAlphaNum(self, c): 
        return (ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9')) 