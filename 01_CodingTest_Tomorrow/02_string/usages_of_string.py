if __name__ == "__main__":
    a = "Hello World"

    # 특정 문자 개수 알려 주기
    print(a.count("l"))  # 3

    # 위치 알려주기, 없으면 -1 반환
    print(a.find("l"))  # 2 ->0부터 시작하므로, 3번째
    print(a.find("!"))  # -1

    # 위치 알려주기, 없으면 ValueError
    print(a.index("l"))
    # print(a.index("!"))  # ValueError: substring not found
    # 따라서, try except 문으로 고치면 좋음
    try:
        print(a.index("!"))  # try to find "!"
    except ValueError:  # handle the case when "!" isn't found
        print("문자열에서 '!' 문자가 포함되어 있지 않음.")

    # 문자열이 숫자로`만` 구성되어있는지, 아닌지를 검사, 숫자로만 구성되어 있으면 True / 아니면 False
    n = "2023"
    print(f'string `{n}`: ', n.isnumeric())

    n = "dfdsfds"
    print(f'string `{n}`: ', n.isnumeric())

    n = "202d3"
    print(f'string `{n}`: ', n.isnumeric())

    # 문자가 알파벳/한글 인지, 숫자인지 검사
    s = "2024, Hello World, python3"
    for char in s:
        print(f'string `{char}`: {"숫자" if char.isnumeric() else "char"}')




    pass
