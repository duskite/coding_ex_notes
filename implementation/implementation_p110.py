from timecheck import time_checked

n = int(input())
directions = input().split()

@time_checked
def my_solve(n , directions):
    direction_dic = {
        'R': (0,1),
        'L': (0,-1),
        'U': (-1,0),
        'D': (1,0)
    }

    position = [1,1]

    for directtion in directions:
        position = list(sum(i) for i in zip(position, direction_dic[directtion]))

        if position[0] < 1:
            position[0] = 1
        if position[1] < 1:
            position[1] = 1

        if position[0] > n:
            position[0] = n
        if position[1] > n:
            position[1] = n

    print(position[0], position[1])


@time_checked
def book_solve(n, plans):
    x, y = 1, 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L','R','U','D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

    print(x, y)

my_solve(n, directions)
book_solve(n, directions)


