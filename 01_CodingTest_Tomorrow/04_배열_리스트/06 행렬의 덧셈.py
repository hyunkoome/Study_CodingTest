"""
행렬의 덧셈

문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

입출력 예
arr1	arr2	return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]
"""


def solution(arr1, arr2):

    answer = [[sub_a+sub_b for sub_a, sub_b in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer


if __name__ == "__main__":
    quiz_dict_list = [
        {"arr1": [[1, 2], [2, 3]], "arr2": [[3, 4], [5, 6]], "return": [[4, 6], [7, 9]]},
        {"arr1": [[1],[2]], "arr2": [[3],[4]], "return": [[4],[6]]},
    ]

    for quiz_dict in quiz_dict_list:
        res = solution(arr1=quiz_dict['arr1'], arr2=quiz_dict['arr2'])
        if res == quiz_dict["return"]:
            print("Correct")
        else:
            print("Wrong")
        print("Solutuin", quiz_dict['return'])
        print("my Solutuin", res)
        print()
