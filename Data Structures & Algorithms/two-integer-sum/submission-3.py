class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)): 
            if nums[i] not in seen: 
                pair = target - nums[i]
                seen[pair] = i 
            else: 
                return [seen[nums[i]], i ]

        return []