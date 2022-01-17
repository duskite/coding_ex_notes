from timecheck import time_checked

n, m, k = map(int, input().split())
data = list(map(int, input().split()))


@time_checked
def my_solve():
    data.sort(reverse=True)

    tmp = m // k
    tmp_n = m % k

    result = 0

    result += data[0] * k * tmp
    result += data[1] * tmp_n

    print(result)


my_solve()
