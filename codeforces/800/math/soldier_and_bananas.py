k, n, w = map(int, input().split())
print(max((w * k * (w + 1)) // 2 - n, 0))
