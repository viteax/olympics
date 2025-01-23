def solve():
    n, m, k = map(int, input().split())
    n, m = n - 1, m - 1
    return (min(n, m) + k - 1) // k + (max(n, m) - min(n, m) + k - 1) // k


print(solve())
