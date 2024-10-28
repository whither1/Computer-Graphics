import numpy as np


def get_line_coeffs(point1, point2):
    x = np.array([point1[0], point2[0]])
    y = np.array([point1[1], point2[1]])

    coeffs = np.polyfit(x, y, 1)
    print(*coeffs)

    return coeffs


def get_edge_points(size, point1, point2):
    coeffs_main = get_line_coeffs(point1, point2)
    x1 = -coeffs_main[1] / coeffs_main[0] if coeffs_main[0] else None
    x2 = (size[1] - coeffs_main[1]) / coeffs_main[0] if coeffs_main[0] else None
    y1 = coeffs_main[1]
    y2 = coeffs_main[0] * size[0] + coeffs_main[1]

    edge_points = []

    if x1 and 0 <= round(x1) <= size[0]:
        edge_points.append((round(x1), 0))

    if x2 and 0 <= round(x2) <= size[0]:
        edge_points.append((round(x2), size[1]))

    if y1 and 0 <= round(y1) <= size[1]:
        edge_points.append((0, round(y1)))

    if y2 and 0 <= round(y2) <= size[0]:
        edge_points.append((size[0], round(y2)))

    return edge_points[0], edge_points[1]


def solve(points):
    min_diff = len(points)
    ans_points = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            coeffs = get_line_coeffs(points[i], points[j])

            lower = 0
            upper = 0
            for k in range(len(points)):
                if k != j and k != i:
                    if coeffs[0] * points[k][0] + coeffs[1] < points[k][1]:
                        lower += 1
                    elif coeffs[0] * points[k][0] + coeffs[1] > points[k][1]:
                        upper += 1
            if abs(lower - upper) < min_diff:
                min_diff = abs(lower - upper)
                ans_points = [points[i], points[j]]

    return ans_points
