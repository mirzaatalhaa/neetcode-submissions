class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for a in strs:
            b= "".join(sorted(a))
            if b not in group:
                group[b]=[a]
            else:
                group[b].append(a)
        return list(group.values())