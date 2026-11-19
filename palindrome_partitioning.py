class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        # Create our backtrack function
        # for now ill only pass in i and see if i need anything more
        def backtrack(start):
            # our return condition should be if len path = len s
            if start == len(s):
                # we return the substring as a list so use .copy()
                res.append(path.copy())
                return
            
            # at any stage, we either pick this palindromic substring or extend it
            for end in range(start, len(s)):
                if isPalindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()

        # helper to determine if s is a palindrome
        def isPalindrome(s):
            return s == s[::-1]
        
        backtrack(0)
        return res
