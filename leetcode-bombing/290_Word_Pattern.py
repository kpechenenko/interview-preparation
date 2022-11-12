class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        recoder = [None for i in range(26)]
        used = set()
        shift = ord('a')
        for p, w in zip(pattern, words):
            p_index = ord(p) - shift
            if not recoder[p_index] and w not in used:
                recoder[p_index] = w
                used.add(w)
            elif recoder[p_index] != w:
                return False
        return True

