# Valid sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Going to use a dictionary
        '''

        spaces = {}

        rowi = 0
        for row in board:
            for col in range(len(row)):
                if row[col] == ".":
                    continue
                
                # Rows
                key = "R" + str(row) + row[col]
                if key in spaces:
                    return False
                spaces[key] = 1

                # Cols
                key = "C" + str(col) + row[col]
                if key in spaces:
                    return False
                spaces[key] = 1

                # Box
                key = "B" + str((rowi//3)*3 + col // 3) + row[col]
                if key in spaces:
                    return False
                spaces[key] = 1

            rowi +=1
        
        return True
