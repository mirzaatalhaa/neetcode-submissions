class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = {}
        size = len(nums) // 3
        res = []
       

        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1

            if seen[i] > size and i not in res:
                res.append(i)
        return res
        
        