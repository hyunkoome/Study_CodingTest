"""
345. Reverse Vowels of a String

Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"



Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

# 해설 강의: https://youtu.be/uHYjUMR3Tg8?si=eniGTJT-MjgyXtkD

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        inputed_vowels_str = []
        for w in s:
            if w in vowels:
                inputed_vowels_str.append(w)
        ivs_inputed_vowels_str = inputed_vowels_str[::-1]

        ans = []
        pos = 0
        for w in s:
            if w in vowels:
                ans.append(ivs_inputed_vowels_str[pos])
                pos += 1
            else:
                ans.append(w)
        return "".join(ans)

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "aeiouAEIOU"
        left_idx = 0
        right_idx = len(s) - 1

        while (left_idx < right_idx):
            if s[left_idx] not in vowels:
                left_idx += 1
            elif s[right_idx] not in vowels:
                right_idx -= 1
            else:
                s[left_idx], s[right_idx] = s[right_idx], s[left_idx]

                left_idx += 1
                right_idx -= 1

        return "".join(s)