class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create dictionaries to store character counts
        s_count = {}
        t_count = {}
        
        # Count characters in string s
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
            
        # Count characters in string t
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
            
        # Compare the character counts
        return s_count == t_count