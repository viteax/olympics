# https://informatics.msk.ru/mod/statements/view.php?chapterid=112430#1

# Задача №112430. Треугольник максимальной площади
# tags: Геометрия

# Суть задачи: найти треугольник максимальной площади
# с вершинами в заданных n точках на плоскости

from math import hypot


def get_ans(n):
    def get_square(a, b, c):
        if sum([a, b, c]) - max([a, b, c]) < max([a, b, c]):
            return 0

        p = (a + b + c) / 2
        s = p * (p - a) * (p - b) * (p - c)
        return s**0.5

    def get_sides(points):
        sides = [
            hypot(points[i][0] - points[i + 1][0], points[i][1] - points[i + 1][1])
            for i in range(-1, 2)
        ]
        return sides

    if n < 3:
        return 0

    points = [list(map(int, input().split())) for _ in range(3)]
    max_s = get_square(*get_sides(points))
    for _ in range(n - 3):
        point = list(map(int, input().split()))
        for i in range(3):
            old = points[i]
            points[i] = point
            s = get_square(*get_sides(points))
            if s < max_s:
                points[i] = old
            max_s = max(s, max_s)
    return max_s


print(get_ans(int(input())))
