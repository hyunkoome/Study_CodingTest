"""
문제 설명
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

제한사항
0 ≤ n ≤ 1,000,000

입출력 예
n   	result
1234	10
930211	16

입출력 예 설명

입출력 예 #1
1 + 2 + 3 + 4 = 10을 return합니다.

입출력 예 #2
9 + 3 + 0 + 2 + 1 + 1 = 16을 return합니다.
"""

def solution(n):
    # n 이 int 일수도 있어서, str(n) 해줘야 함
    return sum(list(map(int, str(n))))

if __name__ == '__main__':
    quiz_dict_list = [
        {"n": "1234", "result": 10},
        {"n": "930211", "result": 16},
    ]

    for quiz_dict in quiz_dict_list:
        res = solution(n=quiz_dict['n'])
        if res == quiz_dict["result"]:
            print("Correct")
        else:
            print("Wrong")

            print()