class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for ch in s:
            sMap[ch] = sMap.get(ch, 0) + 1
        for ch in t:
            tMap[ch] = tMap.get(ch, 0) + 1
        return sMap == tMap
