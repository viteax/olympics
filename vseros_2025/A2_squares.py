def solve():
    d, l, r = map(int, input().split())
    ans = 0
    for a in range(1, int(d**0.5) + 1):
        if d % a != 0 or (d // a - a) % 2 != 0:
            continue

        b = d // a
        y = (b - a) // 2
        x = y + a
        if l <= y**2 and x**2 <= r:
            ans += 1
    return ans


print(solve())
