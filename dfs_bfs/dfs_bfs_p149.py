n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

# 상 우 하 좌 : 시계방향으로
x = [0, 1, 0, -1]
y = [-1, 0, 1, 0]

cnt = 0

def dfs(position):
    # 방문처리
    graph[position[0]][position[1]] = 1

    for i in range(4):
        dx = x[i] + position[0]
        dy = y[i] + position[1]

        # 여기서 dx가 n보다 작아야하는 이유 기억하기
        # for i in range(n)을 도는 i가 x인거임
        if dx >= 0 and dy >=0 and dx < n and dy < m:
            if not graph[dx][dy] == 1:
                dfs((dx, dy))


for i in range(n):
    for j in range(m):
        if not graph[i][j] == 1:
            dfs((i,j))
            cnt += 1

print(cnt)