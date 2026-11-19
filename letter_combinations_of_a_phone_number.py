class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        path = []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for s in mapping[digits[i]]:
                path.append(s)
                backtrack(i+1)
                path.pop()
        
        if not digits:
            return[]
            
        backtrack(0)
        return res
            
