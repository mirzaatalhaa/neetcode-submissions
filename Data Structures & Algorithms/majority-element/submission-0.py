class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       seen = {}
       size = len(nums) // 2
       res, maxc = 0, 0

       for i in nums:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1

        if seen[i] > size:
            return i
        