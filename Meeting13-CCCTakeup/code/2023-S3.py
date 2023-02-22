# CCC '23 S3 - Roy Zhang
import math

NMRC = input().split(" ")
N, M, R, C = int(NMRC[0]), int(NMRC[1]), int(NMRC[2]), int(NMRC[3])

# initialize grid
grid = []
for i in range(N):
    grid.append([0] * M)

# impossible case
if (R == N and C % 2 != 0 and M % 2 == 0) or (C == M and R % 2 != 0 and N % 2 == 0):
    print("IMPOSSIBLE")
else:
    # col palindromes
    count = 0
    if C % 2 == 1 and M % 2 == 1:
        for i in range(N):
            grid[i][M//2] = 'a'
        C -= 1
        count += 1

    # col palindromes
    for j in range(C):
        for i in range(N):
            if j % 2 == 0:
                col_coord = math.ceil(j / 2)
            else:
                col_coord = M - math.ceil(j / 2)
            grid[i][col_coord] = "a"

    # row palindromes
    for i in range(R):
        if i == 0:
            grid[i] = ['a'] * M
        else:
            for j in range(M):
                if grid[i][j]: continue
                if grid[i][M - j - 1]:
                    grid[i][j] = grid[i][M - j - 1]
                else:
                    grid[i][j] = 'b'

    # remaining cells
    for i in range(N):
        for j in range(M):
            if grid[i][j]: continue
            if i == 0:
                grid[i][j] = 'f'
                if not grid[i][M - j - 1]:
                    grid[i][M - j - 1] = 'g'
            elif i % 2 == 0:
                grid[i][j] = 'c'
                if not grid[i][M - j - 1]:
                    grid[i][M - j - 1] = 'd'
            else:
                grid[i][j] = 'd'
                if not grid[i][M - j - 1]:
                    grid[i][M - j - 1] = 'c'

    # special cases
    if C + count == M and R == 0:
        for i in range(N):
            grid[i][-1] = "e"

    elif C + count == M and R != 0:
        for i in range((N - R) // 2):
            grid[i][0] = "e"
            grid[N - i - 1][0] = 'e'

    # print ans
    for row in grid:
        print("".join(str(i) for i in row))
