class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) 
        cols = defaultdict(set) 
        boxes = defaultdict(set) 

        for i in range(len(board)): 
            for j in range(len(board)): 
                el = board[i][j]
                if el == ".": 
                    continue 
                bid = (i//3, j //3)
                if el in rows[i] or el in cols[j] or el in boxes[bid]: 
                    return False
                rows[i].add(el)
                cols[j].add(el)
                boxes[bid].add(el)
                
        return True 