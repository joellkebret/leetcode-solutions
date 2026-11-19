class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = [] 
        path = []

        def backtrack(i,total):
            if total == target:
                res.append(path.copy())
                return

            if i == len(candidates):
                return

            if i == len(candidates) or candidates[i] > target - total:
                return
            # Take the number at this index
            path.append(candidates[i])
            # only using each index one 
            backtrack(i+1, total + candidates[i])
            path.pop()

            next_i = i+1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i+=1
            backtrack(next_i, total )
        
        candidates.sort()
        backtrack(0,0)
        return res
            
