class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        res = []

        for r in range(len(nums)):
            # remove indices that fell out of the window
            while dq and dq[0] < r - k + 1:
                dq.popleft()

            # remove smaller values from the back — they'll never be the max
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            dq.append(r)

            # window is full, record the max (always at the front)
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res