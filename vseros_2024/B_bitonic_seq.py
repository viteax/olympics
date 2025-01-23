def solve(n, a) -> int:
    ans = 0
    is_raise = True
    cur_count = 0

    for i in range(n - 1):
        cur_count += 1
        if a[i] == a[i + 1]:
            ans += (cur_count + 1) * cur_count // 2
            cur_count = 0
        elif is_raise and a[i] > a[i + 1]:
            is_raise = False
        elif not is_raise and a[i] < a[i + 1]:
            ans += (cur_count + 1) * cur_count // 2 - 1
            is_raise = True
            cur_count = 1
    cur_count += 1
    ans += (cur_count + 1) * cur_count // 2

    return ans


n = int(input())
a = list(map(int, input().split()))
ans = solve(n, a)
print(ans)
