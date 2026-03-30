class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = {}
        if len(s) == len(t):
            for ch in s:
                freqMap[ch] = freqMap.get(ch, 0) + 1
        else:
            return False
        
        for ch in t:
            if freqMap.get(ch, 0) == 0:
                break
            freqMap[ch] -= 1

            
        else:
            return True
        return False