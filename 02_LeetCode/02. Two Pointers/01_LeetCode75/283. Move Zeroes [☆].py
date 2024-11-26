"""
283. Move Zeroes

Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""

# 문제 해설: https://youtu.be/BPb0q5J4u-k?si=0_4Fg-ZUT5MXQYK4

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_idx = 0

        for right_idx in range(len(nums)):
            if nums[right_idx] != 0:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
                left_idx += 1