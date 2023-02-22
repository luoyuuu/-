class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        for i in range(len(s)):
            right = right - i
            a = self.slide_window(s,left, right)
            if a:
                return a
            left = 0
            right = len(s) - 1

    def slide_window(self,s,left, right):
        while right >= 0 and right <= len(s) - 1:
            if s[left:right + 1] == s[left:right + 1][::-1]:
                return s[left:right + 1]
            left = left + 1
            right = right + 1