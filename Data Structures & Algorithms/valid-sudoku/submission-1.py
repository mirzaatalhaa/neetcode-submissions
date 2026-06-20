class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue
                elif item in s:
                    return False
                else:
                    s.add(item)

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item == ".":
                    continue
                elif item in s:
                    return False
                else:
                    s.add(item)

        for row in range(0,9,3):
            for col in range(0,9,3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        item = board[row + i][col + j]
                        if item == ".":
                            continue
                        elif item in s:
                            return False
                        else:
                            s.add(item)
        return True
                


