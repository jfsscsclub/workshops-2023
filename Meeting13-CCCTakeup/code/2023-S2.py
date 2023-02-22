# CCC '23 S2 - Roy Zhang
N = int(input())
hills = [int(i) for i in input().split(" ")]

# initialize grid
grid = []
for i in range(N):
    grid.append([0] * N)

# solve
ans = [float('infinity')] * N
ans[0] = 0
for j in range(1, N):
    for i in range(j - 1, -1, -1):
        grid[i][j] = grid[i + 1][j - 1] + abs(hills[i] - hills[j])
        if grid[i][j] < ans[j - i]:
            ans[j - i] = grid[i][j]

print(" ".join(str(i) for i in ans))

# Below is an alternative solution

# CCC '23 S2 - William Shen
n = int(input())
heights = list(map(int, input().split()))
ans = [1000000000000] * (n + 5)
for i in range(n):
    cur = 0
    for j in range(n + 1):
        if i - j < 0 or i + j >= n:
            break
        cur += abs(heights[i - j] - heights[i + j])
        ans[2 * j + 1] = min(ans[2 * j + 1], cur)
for i in range(n):
    cur = 0
    for j in range(n + 1):
        if i - j < 0 or i + j + 1>= n:
            break
        cur += abs(heights[i - j] - heights[i + j + 1])
        ans[2 * j + 2] = min(ans[2 * j + 2], cur)
print(*ans[1:n + 1])