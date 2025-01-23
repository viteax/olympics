def sum_next(s, i, a: list):
    pass


h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
s = int(input())

if sum(a[0]) > s:
    print("NO")
elif sum(a[0]) == s:
    print("YES")
    print(0)
else:
    target = sum(a[0]) - s
    sum_next()
