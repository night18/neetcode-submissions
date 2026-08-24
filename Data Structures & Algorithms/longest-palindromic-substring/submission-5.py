class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        p_len = 1
        p_index = 0

        for i in range(n):
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (i - j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if p_len < (i - j + 1):
                        p_index = j
                        p_len = i - j + 1

        return s[p_index: p_index + p_len]