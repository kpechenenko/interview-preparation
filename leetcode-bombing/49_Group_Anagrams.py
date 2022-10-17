class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for s in strs:
            s_hash = self._calculate_hash(s)
            if s_hash in anagrams:
                anagrams[s_hash].append(s)
            else:
                anagrams[s_hash] = [s]
        return [anagrams[s_hash] for s_hash in anagrams]

    def _calculate_hash(self, s):
        return ''.join(sorted(s))
