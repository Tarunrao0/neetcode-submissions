class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = 0
            mp[nums[i]] += 1

        return sorted(mp.keys(), reverse=True, key= mp.get)[:k]