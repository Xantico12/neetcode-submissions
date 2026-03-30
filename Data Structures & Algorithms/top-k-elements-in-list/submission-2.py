class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        buckets = {}
        max_freq = 0
        for x, c in freq.items():
            if c not in buckets:
                buckets[c] = []
            buckets[c].append(x)
            if c > max_freq:
                max_freq = c

        res = []
        for f in range(max_freq, 0, -1):
            if f in buckets:
                for x in buckets[f]:
                    res.append(x)
                    if len(res) == k:
                        return res