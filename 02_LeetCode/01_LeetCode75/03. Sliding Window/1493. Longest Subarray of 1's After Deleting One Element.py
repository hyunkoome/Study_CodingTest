"""
1493. Longest Subarray of 1's After Deleting One Element
Medium
Topics
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

Hint 1
Maintain a sliding window where there is at most one zero in it.

해설 강의: https://youtu.be/ufJZCvlzo0Y?si=0cFSNBqbg0b_Peoz
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l = 0
        num_zero = 0
        max_w = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1

            while num_zero > 1:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1

            w = r - l + 1 - 1

            max_w = max(max_w, w)

        return max_w
