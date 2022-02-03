n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1