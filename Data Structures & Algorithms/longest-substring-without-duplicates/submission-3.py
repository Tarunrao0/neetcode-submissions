class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        window = set()
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest_substring = max(longest_substring, len(window))

        return longest_substring