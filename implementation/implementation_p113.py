from timecheck import time_checked

n = int(input())

@time_checked
def my_solve(n):
    h, m, s = n, 59, 59
    cnt = 0

    while h >= 0:

        if s < 0:
            m -= 1
            s = 59
        if m < 0:
            h -= 1
            m = 59

        check = str(h) + str(m) + str(s)

        if '3' in check:
            cnt += 1

        s -= 1

    print(cnt)

@time_checked
def book_solve(n):
    count = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count +=1

    print(count)

my_solve(n)
book_solve(n)
