class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(i, total):
            # is valid
            if total == target:
                res.append(path.copy())
                return
            
            # cant be valid
            if i == len(candidates) or total > target:
                return

            # Choice 1: add the number, allow us to pick it again
            path.append(candidates[i])
            backtrack(i, total + candidates[i])

            # Choice 2: dont pick it
            path.pop()
            backtrack(i+1, total)
        
        backtrack(0,0)
        return res
