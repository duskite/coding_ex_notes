

input_data = input()
col = ord(input_data[0]) - ord('a') + 1
row = int(input_data[1])

steps = [(2,-1),(2,1),(-2,-1),(-2,1),(1,-2),(1,2),(-1,-2),(-1,2)]

cnt = 0

for step in steps:
    tmp_col = col + step[0]
    tmp_row = row + step[1]

    if tmp_row < 1 or tmp_row > 8 or tmp_col < 1 or tmp_col > 8:
        continue

    cnt += 1

print(cnt)