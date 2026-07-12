class Solution:
    def isRowValid(self, board: List[List[str]], y: int):
        num_check = [0] * 9
        for x in range(9):
            if board[y][x] != '.':
                num_check[int(board[y][x]) - 1] += 1
        
        for i in range(9):
            if num_check[i] > 1:
                return False
        
        return True
        

    def isColValid(self, board: List[List[str]], x: int):
        num_check = [0] * 9
        for y in range(9):
            if board[y][x] != '.':
                num_check[int(board[y][x]) - 1] += 1
        
        for i in range(9):
            if num_check[i] > 1:
                return False
        
        return True
    
    def isBoxValid(self, board: List[List[str]], y: int, x: int):
        num_check = [0] * 9

        for i in range(3):
            for j in range(3):
                if board[y+i][x+j] != '.':
                    num_check[int(board[y + i][x + j]) - 1] += 1

        for i in range(9):
            if num_check[i] > 1:
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isRowValid(board, i):
                return False
            if not self.isColValid(board, i):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isBoxValid(board, i, j):
                    return False

        return True