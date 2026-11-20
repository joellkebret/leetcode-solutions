class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        jumps = 0

        for num in nums:
            
            if jumps < 0:
                return False
            
            if num >= jumps:
                jumps = num
            
            jumps -=1
        
        return True
