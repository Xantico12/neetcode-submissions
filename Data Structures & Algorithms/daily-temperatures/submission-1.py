class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        result = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1

            while j < n and temps[j] <= temps[i]:
                if result[j] == 0:
                    j = n
                    break
                j += result[j]

            if j < n:
                result[i] = j - i
        return result