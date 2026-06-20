class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            s_num = sorted(nums)
        current = 1
        longest = 1
        for i in range(len(s_num)-1):
            if s_num[i+1] - s_num[i] == 0:
                pass
            elif s_num[i+1] - s_num[i] == 1:
                current+=1
                longest = max(longest, current)
            else:
                current = 1

        return longest
        