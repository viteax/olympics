# https://leetcode.com/problems/find-maximum-area-of-a-triangle/description/


class Solution:
    def maxArea(self, coords: list[list[int]]) -> int:
        LIM = [[10**6 + 1, 10**6 + 1]]

        def get_max_s_by_x(coords, mx, mn, inv=0):
            max_s = 0
            cur_base = 0
            prev = coords[0]
            for coord in coords:
                if coord[0 + inv] != prev[0 + inv]:
                    s = cur_base * max(
                        abs(mx - prev[0 + inv]),
                        abs(mn - prev[0 + inv]),
                    )
                    max_s = max(s, max_s)
                    cur_base = 0
                else:
                    cur_base += coord[1 - inv] - prev[1 - inv]
                prev = coord
            return max_s

        by_x = sorted(coords, key=lambda point: (point[0], point[1]))
        by_y = sorted(coords, key=lambda point: (point[1], point[0]))

        min_x = by_x[0][0]
        max_x = by_x[-1][0]
        min_y = by_y[0][1]
        max_y = by_y[-1][1]

        if min_x == max_x or min_y == max_y:
            return -1

        by_x += LIM
        by_y += LIM

        max_s = get_max_s_by_x(by_x, max_x, min_x)
        max_s = max(get_max_s_by_x(by_y, max_y, min_y, inv=1), max_s)

        return max_s if max_s else -1
