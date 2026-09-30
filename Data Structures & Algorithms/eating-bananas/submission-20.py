import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        
        minK, maxK = 1, max(piles)
        k = maxK
        
        while minK <= maxK:
            midK = (maxK + minK) // 2
            currH = 0
            for p in piles:
                currH += math.ceil(p / midK)
                if currH > h:
                    minK = midK + 1
                    break

            if currH <= h:
                k = midK
                maxK = midK - 1
                
        return k
    
                