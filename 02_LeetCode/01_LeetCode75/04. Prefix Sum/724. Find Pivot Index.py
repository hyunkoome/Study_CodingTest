"""
724. Find Pivot Index
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.



Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0


Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000


Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/

Hint 1
Create an array sumLeft where sumLeft[i] is the sum of all the numbers to the left of index i.
Hint 2
Create an array sumRight where sumRight[i] is the sum of all the numbers to the right of index i.
Hint 3
For each index i, check if sumLeft[i] equals sumRight[i]. If so, return i. If no such i is found, return -1.

강의: https://youtu.be/u89i60lYx8U?si=9W_Y2ep3g3uAtE58
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = 0

        for i in range(len(nums)):
            r_sum += nums[i]

        p_i = -1

        for i in range(len(nums)):
            if i != len(nums) - 1:
                r_sum -= nums[i]
            else:
                r_sum = 0

            if i != 0:
                l_sum += nums[i - 1]
            else:
                l_sum = 0

            if l_sum == r_sum:
                p_i = i
                print(i)
                return i

        return p_i







