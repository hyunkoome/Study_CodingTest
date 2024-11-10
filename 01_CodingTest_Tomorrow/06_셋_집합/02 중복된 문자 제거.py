"""
중복된 문자 제거

문제 설명
문자열 my_string이 매개변수로 주어집니다.
my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ my_string ≤ 110
my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.
대문자와 소문자를 구분합니다.
공백(" ")도 하나의 문자로 구분합니다.
중복된 문자 중 가장 앞에 있는 문자를 남깁니다.

입출력 예
my_string	result
"people"	"peol"
"We are the world"	"We arthwold"

입출력 예 설명

입출력 예 #1
"people"에서 중복된 문자 "p"와 "e"을 제거한 "peol"을 return합니다.

입출력 예 #2
"We are the world"에서 중복된 문자 "e", " ", "r" 들을 제거한 "We arthwold"을 return합니다.
"""

from collections import defaultdict

def solution(my_string):
    words = defaultdict(int)
    answer = ''
    for ch in my_string:
        if words[ch] == 0:
            answer += ch
            words[ch] += 1
    return answer


if __name__ == "__main__":
    quiz_dict_list = [
        {"my_string": "people", "result": "peol"},
        {"my_string": "We are the world", "result": "We arthwold"},
    ]

    for quiz_dict in quiz_dict_list:
        res = solution(my_string=quiz_dict['my_string'])
        if res == quiz_dict["result"]:
            print("Correct")
        else:
            print("Wrong")
        print("Solution", quiz_dict['result'])
        print("my Solution", res)
        print()
