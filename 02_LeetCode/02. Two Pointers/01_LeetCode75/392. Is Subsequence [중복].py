"""
392. Is Subsequence
Attempted
Easy
Topics
Companies
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
# 해설 강의: https://youtu.be/99RVfqklbCE?si=N7wXojPfseeFvTvV

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while(i<len(s) and j<len(t)):
            # if s[i] == t[j]:
            #     i+=1
            #     j+=1
            # else:
            #     j+=1

            if s[i] == t[j]:
                i+=1
                # j+=1
            # else:
            #     j+=1
            j+=1

        if(i==len(s)):
            return True
        else:
            return False


    def isSubsequence_hkkim(self, s: str, t: str) -> bool:
        s_idx = 0
        cnt = 0

        if len(s) == 0:
            return True

        for t_idx in range(len(t)):
            if s_idx == len(s):
                break

            if s[s_idx] == t[t_idx]:
                s_idx += 1
                cnt += 1

        if cnt == len(s):
            return True
        else:
            return False




