class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        longest = 0
        i = 0
        current_starter = -1

        while i < len(s):
            c = s[i]
            
            if c in my_dict:
                current_starter = max(my_dict[c], current_starter)

            my_dict[c] = i
            longest = max(i - current_starter, longest)
            i += 1

        return longest

# abba
# [a: 0, b: 1], starter = -1
# [a: 0, b: 2], starter = 1
# [a: 3, b: 2], starter = 1