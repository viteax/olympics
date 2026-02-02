t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print((b - a % b) % b)

# t = int(input())
# ans_list = []
# for i in range(t):
#     a, b = map(int, input().split())
#     ans = (b - (a % b)) % b
#     ans_list.append(ans)
# print(*ans_list, sep="\n")
