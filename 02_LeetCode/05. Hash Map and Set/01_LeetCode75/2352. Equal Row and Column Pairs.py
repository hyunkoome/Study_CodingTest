"""
2352. Equal Row and Column Pairs
Medium
Topics
Companies
Hint
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105

Hint 1
We can use nested loops to compare every row against every column.
Hint 2
Another loop is necessary to compare the row and column element by element.
Hint 3
It is also possible to hash the arrays and compare the hashed values instead.

해설 강의: https://youtu.be/6cifzEaEEX8?si=-X95OV2zq8F5QGRL
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ## solution 1
        # ans = 0
        # for g in grid:
        #     for r_idx in range(len(grid)):
        #         new_grid = []
        #         for c_idx in range(len(grid[0])):
        #             new_grid.append(grid[c_idx][r_idx])
        #         # print(new_grid)
        #         if g == new_grid:
        #             ans+=1
        # return ans

        ## solution 2
        # count = 0
        # n = len(grid)
        # for r in range(n):
        #     for c in range(n):
        #         is_match = True

        #         for i in range(n):
        #             if grid[r][i] != grid[i][c]:
        #                 is_match = False
        #                 break

        #         if is_match:
        #             count += 1
        # return count

        # ## solution 3
        # n = len(grid)
        # # 행을 튜플로 변환하여 저장
        # rows = [tuple(row) for row in grid]
        # columns = []
        # for c in range(n):
        #     columns.append(tuple([grid[i][c] for i in range(n)]))
        # # 행과 열을 비교하여 동일한 배열을 찾기
        # count = 0
        # for row in rows:
        #     count += columns.count(row)
        # return count

        ## solution 4
        # # 행을 튜플로 변환하여 저장
        # rows = [tuple(row) for row in grid]
        # # 열을 튜플로 변환하여 저장
        # columns = [tuple(grid[i][j] for i in range(len(grid))) for j in range(len(grid))]
        # # 행과 열을 비교하여 동일한 배열을 찾기
        # count = 0
        # for row in rows:
        #     count += columns.count(row)
        # return count

        # ## solution 5
        # n = len(grid)
        # # 행을 튜플로 변환하여 저장
        # rows = [tuple(row) for row in grid]
        # # 만약 동일한 열이 rows에 여러 번 존재하면,
        # # 이 코드에서는 중복된 경우까지 모두 세지 않기 때문에 누락 가능성
        # # 행 빈도 계산후, 열빈도와 매칭해야함
        # row_count = Counter(rows)
        # count = 0
        # for c in range(n):
        #     col = tuple([grid[i][c] for i in range(n)])
        #     if col in rows:
        #         print(col)
        #         # count += 1
        #         count += row_count[col]
        # return count

        # solution 6
        count = 0
        n = len(grid)
        # row.get(tuple(grid[i]), 0): row 딕셔너리에서 해당 행의 빈도를 가져옵니다.
        # 만약 처음 등장하는 행이라면 기본값 0을 사용합니다.
        # 1 + row.get(...): 현재 행의 빈도에 1을 더해 업데이트합니다.
        # 각 행이 몇 번 나타나는지 계산하여 row 딕셔너리에 저장합니다.
        # => 즉, Counter 와 동일
        row = {}
        for i in range(n):
            row[tuple(grid[i])] = 1 + row.get(tuple(grid[i]), 0)

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            if tuple(col) in row:
                count += row[tuple(col)]
        return count






