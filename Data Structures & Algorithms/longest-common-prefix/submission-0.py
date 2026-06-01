class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):       # iterate over characters of first string
            for s in strs[1:]:              # check that character against every other string
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix           # mismatch or string too short, stop here
            prefix += strs[0][i]            # all strings matched at position i

        return prefix