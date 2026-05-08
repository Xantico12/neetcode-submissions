import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        n = len(piles)

        minK, maxK = 1, piles[n - 1]
        k = maxK
        while minK <= maxK:
            midK = (maxK + minK) // 2
            currentH = 0

            for p in piles:
                currentH += math.ceil(p / midK)
                if currentH > h:
                    minK = midK + 1
                    break
            
            if currentH <= h:
                k = midK
                maxK = midK - 1
                    
            
        return k

        # upper boundary for k: piles.sort()[-1]
        # math.ceil(x / k)

        # max hours per pile: maxHours = math.ceil(h / n)
        # kMax = math.ceil(piles[-1] / maxHours)
        # kMin = 1
        # math.ceil(k / (k / math.ceil(h / n)))