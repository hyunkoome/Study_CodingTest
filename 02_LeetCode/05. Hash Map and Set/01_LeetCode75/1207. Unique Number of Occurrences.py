"""
1207. Unique Number of Occurrences
Easy
Topics
Companies
Hint
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

Hint 1
Find the number of occurrences of each element in the array using a hash map.
Hint 2
Iterate through the hash map and check if there is a repeated value.

해설:
- https://youtu.be/4XHOBeE_YOU?si=HC37QrP8iu5uqM-M
- https://youtu.be/pQo5AZRbRpE?si=T44W5Nb4tbpzmjhw
"""

from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # hashmap = Counter(arr)
        # hashmap_count = [v for k, v in hashmap.items()]
        # return True if len(hashmap_count) == len(set(hashmap_count)) else False

        hashmap = {} # store index, counter as key: value
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        hashmap_count = list(hashmap.values())
        count_hashmap = {}
        for i in hashmap_count:
            if i in count_hashmap:
                return False
            count_hashmap[i] = 1
        return True

