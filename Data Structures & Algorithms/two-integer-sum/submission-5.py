class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in mp:
                return [mp[difference], i]

            mp[num] = i 