"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d


Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # return "".join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]

        # output = ""
        # l = min(len(word1),len(word2))
        # for i in range(l):
        #     output += word1[i] + word2[i]
        # if len(word1)>l:
        #     output += word1[l:]
        # if len(word2)>l:
        #     output += word2[l:]
        # return output

        ans = ''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
        return ans


if __name__ == '__main__':

    if __name__ == '__main__':
        q = [
            {"word1": "abc", "word2": "pqr", "output": "apbqcr"},
            {"word1": "ab", "word2": "pqrs", "output": "apbqrs"},
            {"word1": "abcd", "word2": "pq", "output": "apbqcd"},
        ]

        sol = Solution()
        for qe in q:
            if sol.mergeAlternately(word1=qe['word1'], word2=qe['word2']) == qe['output']:
                print("Corect answer:", qe['output'])
            else:
                print("My Ans", sol.mergeAlternately(word1=qe['word1'], word2=qe['word2']))
                print("Solution:", qe['output'])