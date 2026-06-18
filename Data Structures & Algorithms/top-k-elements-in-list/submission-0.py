class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for n in nums:
            if n not in group:
                group[n]=1
            else:
                group[n]+=1
        a = list(group.items())
        a.sort(key=lambda x: x[1])
        result=[]

        for n, count in a[-k:]:
            result.append(n)

        return result