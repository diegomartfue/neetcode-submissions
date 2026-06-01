class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1  # tally up characters in s

        for c in t:
            count[c] = count.get(c, 0) - 1  # subtract for each character in t
            if count[c] < 0:
                return False                 # t has a char s doesn't, or too many

        return True