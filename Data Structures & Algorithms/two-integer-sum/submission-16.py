class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in diff_map:
                return [diff_map[diff], idx]
            diff_map[num] = idx
        return []
        
