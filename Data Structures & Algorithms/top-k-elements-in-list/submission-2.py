class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count = Counter(nums)
        sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        return sorted_keys[:k]


        