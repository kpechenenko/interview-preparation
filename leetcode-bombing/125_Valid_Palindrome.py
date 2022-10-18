class Solution:
#    def isPalindrome(self, s: str) -> bool:
#        clear = [ch.lower() for ch in s if ch.isalpha() or ch.isdigit()]
#        clear = ''.join(clear)
#        if len(clear) < 2:
#            return True
#        l = 0
#        r = len(clear) - 1
#        while l < r:
#            if clear[l] != clear[r]:
#                return False
#            l += 1
#            r -= 1
#        return True

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while not self._isValidCh(s[l]) and l < r:
                l += 1
            while not self._isValidCh(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def _isValidCh(self, s: str) -> bool:
        return s.isalpha() or s.isdigit
