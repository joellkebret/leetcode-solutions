class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        # My idea is to look through every row
        # find if there are any obstrocution in every column and diagonal
        # i figure we dont need to pass the col into our backtracking function
        # no 2 queens could ever be on the same row anyways

        # Couldn't figure out how to do it on my own ... 

        # After looking at the editorial
        # maintain a set that tracks the cols, and diaganols that queens exist on
        cols = set()
        posD = set()
        negD = set()
        
        def backtrack(r):
            # our base case should verify if we have placed a queen in this row
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            # iterate over the columns
            for c in range(n):
                if c in cols or (r-c) in posD or (r+c) in negD:
                    continue # a conflict in the diagonals or cols so we skip
                
                # add to our set and recurse
                board[r][c] = 'Q'
                cols.add(c)
                posD.add(r-c)
                negD.add(r+c)

                backtrack(r+1)

                # backtrack
                board[r][c] = '.'
                cols.remove(c)
                posD.remove(r-c)
                negD.remove(r+c)
            
        backtrack(0)
        return res
                



            
