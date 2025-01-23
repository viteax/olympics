ROW_LEN = 6


def solve(n, m, field) -> list[str] | None:
    empty = 0
    new_field = [[field[i][j] for j in range(ROW_LEN)] for i in range(n)]
    for row_no, row in enumerate(field):
        for i in range(ROW_LEN):
            if row[i] != row[-i - 1] and row[-i - 1] == "X":
                m -= 1
                new_field[row_no][i] = "X"
            elif row[i] == ".":
                empty += 1

    if m % 2 == 1 or m > empty or m < 0:
        return None
    i = 0
    j = 0
    while m > 0 and i < n:
        if new_field[i][j] == ".":
            new_field[i][j] = "X"
            new_field[i][-j - 1] = "X"
            m -= 2
        j += 1
        if j == 3:
            i += 1
            j = 0
    new_field = ["".join(new_field[i]) for i in range(n)]
    return new_field


n, m = map(int, input().split())
field = [input() for _ in range(n)]
ans = solve(n, m, field)

if ans:
    for row in ans:
        print(row)
else:
    print("Impossible")
