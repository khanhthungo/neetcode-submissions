class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)): 
            while len(stack) > 0 and stack[-1][0] < temperatures[i]: 
                idx = stack[-1][1]
                res[idx] = i - idx 
                stack.pop()
            stack.append([temperatures[i], i])
        
        return res