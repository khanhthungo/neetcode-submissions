class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerdSt = s.lower()
        l = 0 
        r= len(s)-1
        while l < r: 
            while l < r and not self.isAlphaNum(lowerdSt[l]): 
                l +=1 
            while l < r and not self.isAlphaNum(lowerdSt[r]):
                r-=1
            if lowerdSt[r] != lowerdSt[l]: 
                return False 
            l+=1 
            r-=1 
        return True
        
    def isAlphaNum(self, st): 
        return ((ord('a') <= ord(st) <= ord('z')) or 
                ord('0') <= ord(st) <= ord('9') 
        )