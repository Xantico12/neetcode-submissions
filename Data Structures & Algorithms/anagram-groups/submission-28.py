class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = "".join(sorted(s))

            if key not in groups:
                groups[key] = [s]
            else:
                groups[key] += [s]

        
        anagrams = []
        for k, v in groups.items():
            anagrams.append(v)
        return anagrams