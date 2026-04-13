class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        subF = {}
        windowF = {}
        for c in t:
            subF[c] = subF.get(c, 0) + 1

        missing = len(t)
        bestL, bestR = 0, len(s)
        l = 0

        for r in range(len(s)):
            windowF[s[r]] = windowF.get(s[r], 0) + 1
            if windowF[s[r]] <= subF.get(s[r], 0):
                missing -= 1

            while missing == 0:
                if r - l < bestR - bestL:
                    bestL, bestR = l, r

                windowF[s[l]] -= 1
                if windowF[s[l]] < subF.get(s[l], 0):
                    missing += 1

                l += 1
        
        return s[bestL:bestR + 1] if bestR < len(s) else ""