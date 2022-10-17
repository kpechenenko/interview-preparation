class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_counts = [0 for i in range(26)]
        a_code = ord('a')
        for ch in s:
            letter_counts[ord(ch) - a_code] += 1
        for ch in t:
            letter_counts[ord(ch) - a_code] -= 1
        for cnt in letter_counts:
            if cnt != 0:
                return False
        return True
