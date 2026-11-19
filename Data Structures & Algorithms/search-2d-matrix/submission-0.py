class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) -1 
        while l <= r: 
            m = l + (r-l)//2 
            if target >= matrix[m][0] and target <= matrix[m][-1]: 
                return self.bs(matrix[m][:], target)
            elif target >= matrix[m][-1]: 
                l = m + 1 
            else: 
                r = m - 1
        return False



    def bs(self, arr, target): 
        l = 0 
        r = len(arr) -1 
        while l <= r: 
            m = l + (r-l)//2 
            
            if arr[m] == target: 
                return True
            elif arr[m] < target: 
                l = m + 1 
            else: 
                r = m - 1
        return False 