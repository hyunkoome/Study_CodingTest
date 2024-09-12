"""
문제 설명
문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.

먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다.
처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.

제한사항
1 ≤ s의 길이 ≤ 10,000
s는 영어 소문자로만 이루어져 있습니다.

입출력 예
s               	result
"banana"	        3
"abracadabra"	    6
"aaabbaccccabba"	3

입출력 예 설명

입출력 예 #1
s="banana"인 경우 ba - na - na와 같이 분해됩니다.

입출력 예 #2
s="abracadabra"인 경우 ab - ra - ca - da - br - a와 같이 분해됩니다.

입출력 예 #3
s="aaabbaccccabba"인 경우 aaabbacc - ccab - ba와 같이 분해됩니다.
"""

from collections import deque

def solution(s):
    res_list = []
    res_str_list = []
    que_s = deque(s)
    split_cnt = 0

    while que_s:
        sub_list = []
        sub_str = ''
        first_char = que_s.popleft()  # 첫번째 글자 꺼내기
        cnt_x = 1
        not_x_cnt = 0
        sub_list.append(first_char)
        sub_str += first_char  # 첫 글자를 바로 문자열로 추가

        while que_s:
            crt_char = que_s.popleft()
            if crt_char == first_char:
                cnt_x += 1
            else:
                not_x_cnt += 1

            sub_list.append(crt_char)
            sub_str += crt_char  # 현재 글자를 바로 문자열로 추가

            if cnt_x == not_x_cnt:
                split_cnt += 1
                res_list.append(sub_list)
                res_str_list.append(sub_str)
                break

        if not que_s and (cnt_x != not_x_cnt):
            res_list.append(sub_list)
            res_str_list.append(sub_str)
            split_cnt += 1

    return split_cnt, res_list, res_str_list

if __name__ == '__main__':
    quiz_dict_list = [
        {"s": "banana", "result": 3},
        {"s": "abracadabra", "result": 6},
        {"s": "aaabbaccccabba", "result": 3},
    ]

    for quiz_dict in quiz_dict_list:
        res, res_list, res_str_list = solution(s=quiz_dict['s'])

        print('input: ', quiz_dict['s'], 'Solution: ', quiz_dict['result'])
        if res == quiz_dict["result"]:
            print("Correct")
        else:
            print("Wrong")
        print('my solution: ', res)
        print('results #1: ', res_list, 'results #2: ', res_str_list)
        print()