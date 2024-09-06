
def solution(my_string):
    answer = eval(my_string)
    return answer


if __name__ == "__main__":
    res = solution(my_string="3 + 4")
    if res == 7:
        print("Correct")
    else:
        print("Wrong")