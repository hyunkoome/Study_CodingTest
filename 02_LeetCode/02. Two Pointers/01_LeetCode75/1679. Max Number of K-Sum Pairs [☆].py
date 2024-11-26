"""
1679. Max Number of K-Sum Pairs
Attempted
Medium
Topics
Companies
Hint
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.



Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109

-------------------------------------------------------------

이 문제는 주어진 배열 nums에서 두 수를 더했을 때 k가 되는 쌍을 찾아서 지울 수 있는 최대 횟수를 구하는 문제입니다. 간단히 말해서, 더해서 k가 되는 쌍들을 몇 번이나 만들 수 있는지를 묻고 있어요.

힌트를 한글로 풀이해볼게요.

힌트 설명
Hint 1: 문제는 주어진 합 k가 되는 서로 겹치지 않는(disjoint) 쌍을 구하는 문제라는 점이에요. 즉, 어떤 숫자도 한 번만 사용해서 다른 숫자와 쌍을 만들어야 합니다.

Hint 2: k가 되는 쌍을 만들기 위해서는, 한 숫자 x를 골랐다면, k - x라는 다른 숫자가 필요하다는 점을 활용할 수 있어요. 예를 들어 k = 5이고, x = 2라면 k - x = 3이 되므로, 2와 3이 한 쌍이 되는 식이죠.

Hint 3: 특정 숫자 x와 k - x의 쌍의 개수를 세기 위해서는 각각의 숫자 빈도 수를 최소화해야 해요. 만약 x와 k - x의 빈도를 비교했을 때 min(count(x), count(k - x))만큼의 쌍이 만들어질 수 있습니다.

예를 들어, x = 2, k = 5라면, k - x = 3이므로 2와 3의 빈도를 비교해 더 적은 수를 쌍의 개수로 취할 수 있어요. 예를 들어 2가 3개, 3이 2개 있다면 최대 2개의 쌍을 만들 수 있죠.
단, 만약 x가 k / 2일 경우, 같은 숫자들끼리 쌍을 이뤄야 하므로 count(x) // 2 개의 쌍만 만들 수 있어요.
문제 해결 방법
이제 이 힌트들을 이용한 풀이 방법을 설명할게요.

숫자 빈도 세기: nums 배열에서 각 숫자가 몇 번 나오는지 세기 위해 Counter를 사용하면 편리해요. Counter는 각 숫자의 빈도를 딕셔너리 형태로 저장해줍니다.

각 숫자별 쌍 만들기:

Counter에서 하나씩 숫자를 가져와서 그 숫자와 k - x 쌍이 얼마나 나올 수 있는지 확인합니다.
이때 min(count(x), count(k - x)) 개수만큼 쌍을 만들고, 그 숫자들을 빈도에서 제거합니다.
특수 케이스 처리 (k / 2일 때):

숫자 x가 k / 2일 경우, 같은 숫자끼리 쌍을 이뤄야 하므로 count(x) // 2 만큼 쌍을 만들 수 있습니다.
최종 결과 반환: 쌍의 개수를 모두 더해서 결과로 반환합니다.
"""

# 해설 강의: https://youtu.be/SP-YdgObPAQ?si=uzxipKAz4at6MFIq

from typing import List
from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        seen = set()
        cnt =0

        for num in c:
            if (num not in seen) and (k-num in c):
                if num == (k-num):
                    cnt += c[num]//2
                else:
                    cnt += min(c[num], c[k-num])
                seen.add(num)
                seen.add(k-num)
        return cnt

    def maxOperationsGPT(self, nums: List[int], k: int) -> int:
        """
        elif x == k - x가 아니라 elif x < k - x가 맞습니다.

        이 조건이 필요한 이유는 x와 k - x가 서로 다른 두 수일 때만 중복해서 쌍을 계산하지 않기 위해서입니다.
        elif x < k - x는 다음과 같은 이유로 적절합니다:

        중복 계산 방지:

        예를 들어, x = 2, k = 5일 때 k - x = 3입니다. x < k - x이므로 2와 3 쌍을 한 번만 계산하게 됩니다.
        만약 elif x == k - x를 사용하면 x < k - x 조건이 없어 중복 계산이 발생할 수 있어요.
        Counter는 숫자 순서대로 순회하기 때문에 2와 3 쌍을 계산하고, 나중에 3을 만났을 때 3과 2 쌍을 다시 계산하게 됩니다.

        특수한 케이스:

        elif x == k - x는 x * 2 = k일 때, 즉 k가 짝수이며 k / 2로 쌍을 이룰 때만 참입니다.
        이 경우는 elif x * 2 == k 조건으로 따로 처리해주고 있기 때문에 elif x < k - x가 필요한 것이죠.
        결론적으로, elif x < k - x는 중복 계산을 방지하면서 유효한 쌍만 계산하도록 합니다.
        """
        counter = Counter(nums)
        operations = 0

        for x in counter:
            if x * 2 == k:  # x와 x로 쌍을 이루는 경우
                operations += counter[x] // 2
            elif x < k - x:  # 서로 다른 두 수로 쌍을 이루는 경우만 계산
                operations += min(counter[x], counter[k - x])

        return operations

if __name__ == '__main__':
    s = Solution()
    print(s.maxOperations(nums=[3,1,3,4,3], k=6))