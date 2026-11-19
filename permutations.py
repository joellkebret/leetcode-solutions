class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []a
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):

                if used[i] == True:
                    continue

                # Add the number now
                used[i] = True
                path.append(nums[i])
                backtrack()

                # or later
                used[i] = False
                path.pop()
        
        backtrack()
        return res
