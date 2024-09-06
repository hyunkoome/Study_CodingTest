"""
문제 설명
문자열 my_string이 매개변수로 주어집니다. 
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ my_string의 길이 ≤ 1,000
1 ≤ my_string 안의 자연수 ≤ 1000
연속된 수는 하나의 숫자로 간주합니다.
000123과 같이 0이 선행하는 경우는 없습니다.
문자열에 자연수가 없는 경우 0을 return 해주세요.

입출력 예
my_string	    result
"aAb1B2cC34oOp"	37
"1a2b3c4d123Z"	133

입출력 예 설명

입출력 예 #1
"aAb1B2cC34oOp"안의 자연수는 1, 2, 34 입니다. 따라서 1 + 2 + 34 = 37 을 return합니다.

입출력 예 #2
"1a2b3c4d123Z"안의 자연수는 1, 2, 3, 4, 123 입니다. 따라서 1 + 2 + 3 + 4 + 123 = 133 을 return합니다.
"""


def solution(my_string):
    jari = 0
    answer = 0
    inverse_my_string = my_string[::-1]
    print(my_string)
    print(inverse_my_string)
    string_check = 0
    nums = []

    for i, c in enumerate(inverse_my_string):
        if c.isnumeric():
            v = (10 ** jari) * int(c)  # 10 제곱 : 10**2
            nums.append(v)
            answer += v
            # print(f"************ {i}: {c} *****************")
            # print(f"nums={nums}")
            # print(f"jari={jari}")
            # print(f"answer={answer}")
            jari += 1
        else:
            nums.append(-1)
            string_check += 1
            # print(f"************ {i}: {c} *****************")
            # print(f"nums={nums}")
            # print(f"string_check={string_check}")
            jari = 0

    if string_check == 0:
        return 0

    print(nums[::-1])
    return answer


def solution2(my_string):
    for i in my_string:
        if i.isalpha():  # 대소문자 관계없이 알파벳인지를 판별하는 함수
            my_string = my_string.replace(i, ' ')

    # split() 인자 없이 사용하여 연속된 공백을 제거
    my_string = my_string.split()  # ['1', '2', '34']
    # my_string = my_string.split(' ')  # ['', '', '', '1', '2', '', '34', '', '', '']


    # map()은 반복 가능한 객체를 반환하는데, 그 자체로는 결과가 보이지 않기 때문에 list()로 변환해서 결과를 확인하는 경우가 많아.
    return sum(list(map(int, my_string)))

if __name__ == '__main__':
    quiz_dict_list = [
        {"quiz": "aAb1B2cC34oOp", "result": 37},
        {"quiz": "1a2b3c4d123Z", "result": 133},
    ]

    for quiz_dict in quiz_dict_list:
        res = solution2(my_string=quiz_dict['quiz'])
        if res == quiz_dict["result"]:
            print("Correct")
        else:
            print("Wrong")

            print()
