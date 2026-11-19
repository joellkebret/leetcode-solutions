class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        starts = []
        m = len(board)
        n = len(board[0])

        # build our possible starts
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append((i,j))
        
        # If no starting letter return false
        if not starts:
            return False
        
        def backtrack(i,j,k):
            # Out of bounds return early
            if i<0 or j<0 or i>=m or j>=n:
                return False
            
            # Not equal return early
            if board[i][j] != word[k]:
                return False

            # Return true
            if k == len(word)-1:
                return True
            
            # Prevent repeating characters
            letter = board[i][j]
            board[i][j] = '#' # this will return early

            found = (
                backtrack(i-1,j,k+1) or
                backtrack(i+1,j,k+1) or
                backtrack(i,j-1,k+1) or
                backtrack(i,j+1,k+1)
            )

            # Restore OG board
            board[i][j] = letter
            return found
        
        for start in starts:
            i,j = start
            if backtrack(i,j,0):
                return True
        return False
