"""
443. String Compression
Medium
Topics
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
# 강의 해설: https://youtu.be/zxYcE1quwG4?si=ttnMRv-cTtPjjy_9

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("EXIT")
        """
        예를 들어, chars = ["a","a","b","b","c","c","c"]라면:
        원래 코드에서는 c 그룹이 끝까지 반복되더라도 else 조건이 실행되지 않아 마지막 "c3"을 배열에 넣지 못해요.
        하지만 chars.append("EXIT")를 하면 마지막에 "EXIT"이 들어가면서 else 블록이 트리거되고, 
        c 그룹이 마무리되어 압축 결과를 배열에 저장하게 됩니다.
        """
        index = 0
        prev_ch = chars[0]
        cnt = 0

        for idx, ch in enumerate(chars):
            if prev_ch == ch:
                cnt += 1
            else:  # change ch 글자 변할때
                if cnt == 1:  # cnt 1이면 문자만 추가하고, 숫자는 추가 안함
                    chars[index] = prev_ch
                    index += 1
                else:  # cnt > 1이면 문자 및 숫자 모두 추가
                    chars[index] = prev_ch
                    index += 1
                    for s in str(cnt):
                        chars[index] = s
                        index += 1

                prev_ch = ch
                cnt = 1
        return index


if __name__ == "__main__":
    s = Solution()
    print(s.compress(chars=["a","a","b","b","c","c","c"]))