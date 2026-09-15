class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float('inf')
        sum = 0 
        l = 0

        for r in range(len(nums)):
            sum += nums[r]

            while sum >= target:
                min_l = min(min_l, r-l+1)
                sum -= nums[l]
                l += 1

        return min_l if min_l < float('inf') else 0