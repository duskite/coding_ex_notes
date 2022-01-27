
n, m = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]

min_list = []

for i in range(n):
    min_list.append(min(data[i]))

print(max(min_list))


