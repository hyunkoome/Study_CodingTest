class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while(stack and a <0 and stack[-1] > 0): # stack[-1] 마지막에 stack 에 넣은것
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0 #  while 문 나옴
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack