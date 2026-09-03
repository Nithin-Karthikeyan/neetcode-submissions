class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        # count = Counter(nums)
        # sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        # return sorted_keys[:k]

        # Using bucket sort
        # Use a hashmap, keys are counts, values are the num thats counted as much as the key
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

        