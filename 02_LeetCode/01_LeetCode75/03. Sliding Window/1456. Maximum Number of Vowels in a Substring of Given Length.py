"""
1456. Maximum Number of Vowels in a Substring of Given Length
Medium
Topics
Companies
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Hint 1
Keep a window of size k and maintain the number of vowels in it.
Hint 2
Keep moving the window and update the number of vowels while moving. Answer is max number of vowels of any window.

강의 해설: https://youtu.be/kEfPSzgL-Ss?si=BBMn8FuRKrY3eGJb
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s_list = list(s)

        vowel = "aeiou"

        max_vowel = 0
        crt_vowel = 0
        for i in range(k):
            crt_vowel += 1 if s[i] in vowel else 0

        max_vowel = crt_vowel

        for i in range(k, len(s_list)):
            crt_vowel += (1 if s[i] in vowel else 0) - (1 if s[i - k] in vowel else 0)

            max_vowel = max(max_vowel, crt_vowel)

        return max_vowel