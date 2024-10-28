"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            LenOfCommonString = math.gcd(len(str1), len(str2)) # gcd 최소공약수(Greatest Common Divisor)
            return str1[:LenOfCommonString]
        else:
            return ""


if __name__ == '__main__':
    q = [
        {"str1": "ABCABC", "str2": "ABC", "output": "ABC"},
        {"str1": "ABABAB", "str2": "ABAB", "output": "AB"},
        {"str1": "LEET", "str2": "CODE", "output": ""},
        {"str1": "ABCDEF", "str2": "ABC", "output": ""},
        ]

    sol = Solution()
    for qe in q:
        if sol.gcdOfStrings(str1=qe['str1'], str2=qe['str2']) == qe['output']:
            print("Corect answer:", qe['output'])
        else:
            print("My Ans", sol.gcdOfStrings(str1=qe['str1'], str2=qe['str2']))
            print("Solution:", qe['output'])


