class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = []
        for i in range(len(position)-1, -1 , -1): 
            # 3 4.5 10 3
            t = (target - position[i])/speed[i]
            res.append([position[i],t])
        res = sorted(res)
        # print(res)
        for i in range(len(res)-1, -1 , -1): 
            if len(stack) <= 0 or res[i][1] > stack[-1][1]: 
                stack.append(res[i])
        return len(stack)