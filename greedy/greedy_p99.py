from timecheck import time_checked

n, k = map(int, input().split())

@time_checked
def my_solve(n, k):

    cnt = 0
    remainder = 0

    while n >= k:
        remainder += (n % k)

        n //= k
        cnt += 1

        if n == 1:
            break

    while n > 1:
        n -= 1
        cnt += 1

    cnt += remainder
    print(cnt)


@time_checked
def book_solve(n, k):
    result = 0

    while n >= k:
        while n % k != 0:
            n -= 1
            result += 1
        n //= k
        result += 1

    while n > 1:
        n -= 1
        result += 1

    print(result)

my_solve(n, k)
book_solve(n, k)
