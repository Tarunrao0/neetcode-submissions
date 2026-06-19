class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = 1
            mp[nums[i]] += 1
        result = sorted(mp, key=mp.get, reverse = True)
        return result[:k]