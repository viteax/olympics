# https://contest.yandex.ru/roiarchive/contest/57926/download/5/


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    is_prime = [True] * (10**6 + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, 10**6 + 1):
        if not is_prime[i]:
            continue
        primes.append(i)
        for j in range(i**2, 10**6 + 1, i):
            is_prime[j] = False
    ans = [2] * n
    for i in range(n):
        if is_prime[a[i]]:
            ans[i] = 1
            continue
        counter = 0
        cur = 0
        while a[i] != 1:
            while a[i] % primes[cur] == 0:
                a[i] //= primes[cur]
                counter += 1
            if is_prime[a[i]]:
                counter += 1
                break
            cur += 1
        if counter % 2 == 1:
            ans[i] = 1
    return ans


ansList = []
ansList.append(solve())

for ans in ansList:
    print(*ans)
