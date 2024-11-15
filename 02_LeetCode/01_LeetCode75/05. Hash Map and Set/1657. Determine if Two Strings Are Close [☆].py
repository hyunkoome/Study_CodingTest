"""
1657. Determine if Two Strings Are Close
Medium
Topics
Companies
Hint
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.



Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"


Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

Hint 1
Operation 1 allows you to freely reorder the string.
Hint 2
Operation 2 allows you to freely reassign the letters' frequencies.

해설 강의: https://youtu.be/0Nt8t75dFl0?si=URAGx6xQxA0G44J5
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Set, word2Set = set(word1), set(word2)

        word1C, word2C = Counter(word1), Counter(word2)

        freq1 = Counter(word1C.values())  # list(word1C.values())
        freq2 = Counter(word2C.values())  # list(word2C.values())

        print(word1C, word2C, word1Set, word2Set, freq1, freq2)

        return (word1C == word2C) or (word1Set == word2Set and freq1 == freq2)


if __name__ == '__main__':
    s = Solution()
    s.closeStrings(word1="abc", word2="bca")