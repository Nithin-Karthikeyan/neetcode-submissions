class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = min_height * (right_index - left_index)
        max_ = 0
        l, r = 0, len(heights)-1

        while l < r:
            new_area = min(heights[l], heights[r]) *  (r-l)
            max_ = max(max_, new_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_