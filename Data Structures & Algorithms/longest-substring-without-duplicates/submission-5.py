class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxlen = 0
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            maxlen = max(r - l + 1, maxlen)

        return maxlen