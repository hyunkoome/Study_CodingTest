"""
334. Increasing Triplet Subsequence
Medium
Topics
Companies
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

# 해설강의:
# https://youtu.be/Nqht7TDjItM?si=YpWvl055ALn91SFm
# https://youtu.be/QBiEJul9bUk?si=KOU4cLA4iWw2ZtqL

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n_smallest = float('inf')  # sys.maxsize
        n_second_smallest = float('inf')  # sys.maxsize

        for n in nums:
            if n <= n_smallest:
                n_smallest = n
            elif n <= n_second_smallest:
                n_second_smallest = n
            else:
                return True

        return False
