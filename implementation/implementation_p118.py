# 답안 예시에서는
# dx, dy로 방향을 정의하고 방문 배열을 별도로 지정
# 맵과 방문 배열이 0일때 방문하는 방식으로 함

n, m = map(int, input().split())
row, col, direction = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(m)]

# 방향 0 북쪽 / 1 동 / 2 남 / 3 서
steps = [(-1,0),(0,1),(1,0),(0,-1)]
cnt = 0
tile_cnt = 0 # 4가 될 경우 모든 곳이 1또는 -1인거임 # 원래 방향을 보게됨

while True:

    # 현재 위치를 방문 처리하고 방문한 칸의 수 증가
    if maps[row][col] == 0:
        maps[row][col] = -1
        cnt += 1

    # 사방이 이미 방문했거나 바다인 경우에는 방향을 바꾸지 않고 기존 방향 유지 // 뒤로 가려고
    if tile_cnt != 4:
        direction -= 1 # 반시계 90도 방향을 봄
    if direction < 0:
        direction = 3

    tmp_row = row + steps[direction][0]
    tmp_col = col + steps[direction][1]

    # 원래방향 보게 됨 # 주변이 바다거나 이미 방문했을때 tile_cnt가 증가했기 때문에
    # 4일 경우 모든 방향이 1인거임
    if tile_cnt >= 4:
        # 뒤로가기
        tmp_row = row - steps[direction][0]
        tmp_col = col - steps[direction][1]

        if maps[tmp_row][tmp_col] == 1:
            break
    # 바다면 패스
    elif maps[tmp_row][tmp_col] == 1 or maps[tmp_row][tmp_col] == -1:
        tile_cnt += 1
        continue

    tile_cnt = 0
    # 바다가 아니면 이동
    row, col = tmp_row, tmp_col

print(cnt)



