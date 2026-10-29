class Solution:
    def trap(self, height: List[int]) -> int:
        gtrapped = 0 
        l = 0 
        r = len(height) -1 
        maxL = height[l] 
        maxR = height[r]

        while l < r : 
            if maxL <= maxR: 
                l +=1 
                water = maxL - height[l]
                if water > 0: 
                    gtrapped += water
                else: 
                    maxL = height[l]
            else: 
                r -=1 
                water = maxR - height[r]
                if water > 0: 
                    gtrapped += water
                else: 
                    maxR = height[r] 
        return gtrapped 
        # currTrapped = min(maxL, maxR) - height[i]