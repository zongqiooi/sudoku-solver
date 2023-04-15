from pprint import pprint

def sudokuSolver(sudoku):
    ROW = len(sudoku)
    COL = len(sudoku[0])
    
    for r in range(ROW):
        for c in range(COL): 
            if sudoku[r][c] == "x": 
                for guess in range(1, 10): 
                    if isValid(sudoku, r, c, guess) == True: 
                        sudoku[r][c] = str(guess)
                        
                        if sudokuSolver(sudoku) == True: # solve recursively 
                            return True 
                        else: 
                            sudoku[r][c] = "x" # backtrack the guess 

                return False # not possible to have solution with previous values, need to backtrack 
    
    return True 
               
def isValid(sudoku, r, c, guess):     
    for i in range(9): 
        if sudoku[r][i] == str(guess): 
            return False 
        if sudoku[i][c] == str(guess):
            return False 
        if sudoku[(((r//3) * 3) + (i//3))][(((c//3) * 3) + (i%3))] == str(guess):
            return False
    return True 

if __name__ == "__main__":
    sudoku = [
        ["5","3","x","x","7","x","x","x","x"], 
        ["6","x","x","1","9","5","x","x","x"],
        ["x","9","8","x","x","x","x","6","x"],
        ["8","x","x","x","6","x","x","x","3"],
        ["4","x","x","8","x","3","x","x","1"],
        ["7","x","x","x","2","x","x","x","6"],
        ["x","6","x","x","x","x","2","8","x"],
        ["x","x","x","4","1","9","x","x","5"],
        ["x","x","x","x","8","x","x","7","9"]
    ] 
    print("Sudoku before solving: ")
    pprint(sudoku)
    sudokuSolver(sudoku)
    print()
    print("Sudoku after solving: ")
    pprint(sudoku)