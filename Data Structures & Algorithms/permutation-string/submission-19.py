class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        l = 0
        subF = {}
        window = {}

        for c in range(len(s1)):
            subF[s1[c]] = subF.get(s1[c], 0) + 1
        
        for c in range(windowSize - 1):
            window[s2[c]] = window.get(s2[c], 0) + 1
        
        for r in range(windowSize - 1, len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1

            if subF == window:
                return True

            window[s2[l]] -= 1

            if window[s2[l]] == 0:
                window.pop(s2[l])
            
            l += 1
            

        return False