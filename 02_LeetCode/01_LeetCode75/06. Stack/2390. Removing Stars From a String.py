class Solution:
    # 강의 해설: https://youtu.be/pRyFZIaKegA?si=Jq6Q1Zui4CjnRaHO
    def removeStars(self, s: str) -> str:
        # # 풀이법은 맞지만, 시간 초과
        # s = list(s)
        # i = 0
        # while(i<len(s)):
        #     if s[i] == '*':
        #         # print(i)
        #         del s[i]
        #         del s[i-1]
        #         i -= 1
        #     else:
        #         i +=1
        # return ''.join(s)

        s = list(s)
        stack = [] # stack 은 위로 쌓음

        for w in s:
            if w == '*': # * 만나면, 최신에 넣은것을 빼면 됨
                stack and stack.pop() # stack 이 empty 가 아니면 pop()
            else:
                stack.append(w)
        return ''.join(stack)


