class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        l = 0
        total = 0

        for r in range(len(nums)):

            
            total += nums[r]

            while total >= target:
                minlen = min(r - l + 1, minlen)
                total -= nums[l]
                l+=1

        return 0 if minlen == float("inf") else minlen
        