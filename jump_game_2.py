class Solution:
    def jump(self, nums: list[int]) -> int:
        # we start at index 0
        # We can jump a max of nums[i] from index i.
        # we will always reach the n-1th index
        # return the min.

        res = 0
        l = r = 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])
            
            l = r+1
            r = farthest
            res+=1
        
        return res
