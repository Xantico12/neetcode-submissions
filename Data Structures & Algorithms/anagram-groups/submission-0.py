class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = "".join(sorted(s))  # canonical key for the anagram group

            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())
