class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1 
        while l < r: 
            can = numbers[l] + numbers[r]
            if can == target: 
                return [l+1,r+1]
            elif can < target: 
                l+=1 
            else: 
                r-=1 
        return []