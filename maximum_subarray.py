class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSubarray = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSubarray = max(currSum,maxSubarray)
        return maxSubarray
