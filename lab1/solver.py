# На плоскости дано множество точек. Найти такой треугольник
# с вершинами в этих точках, для которого разность площадей 
# описанного и вписанного кругов максимальна

import numpy as np
from math import sqrt, pi, acos

EPS = 1e-8

def get_triangle_area(points: list) -> float:
    det = points[0][0] * (points[1][1] - points[2][1]) - \
          points[1][0] * (points[0][1] - points[2][1]) + \
          points[2][0] * (points[0][1] - points[1][1])
    
    return 0.5 * abs(det)

def get_triangle_half_perim(points: list) -> float:
    a1 = sqrt((points[1][1] - points[0][1]) ** 2 + (points[1][0] - points[0][0]) ** 2)
    a2 = sqrt((points[2][1] - points[0][1]) ** 2 + (points[2][0] - points[0][0]) ** 2)
    a3 = sqrt((points[2][1] - points[1][1]) ** 2 + (points[2][0] - points[1][0]) ** 2)
    return 0.5 * (a1 + a2 + a3)

def check_triangle_existance(points: list) -> bool:
    if len(points) > 3:
        return False

    area = get_triangle_area(points)
    
    return abs(area) > EPS

def get_inner_circle_radius(points: list) -> float:
    s = get_triangle_area(points)
    p = get_triangle_half_perim(points)
    return s / p

def get_outer_circle_radius(points: list) -> float:
    s = get_triangle_area(points)
    a1 = sqrt((points[1][1] - points[0][1]) ** 2 + (points[1][0] - points[0][0]) ** 2)
    a2 = sqrt((points[2][1] - points[0][1]) ** 2 + (points[2][0] - points[0][0]) ** 2)
    a3 = sqrt((points[2][1] - points[1][1]) ** 2 + (points[2][0] - points[1][0]) ** 2)
    return (a1 * a2 * a3) / (4 * s)

def solve(points: list) -> list:
    max_diff = 0
    ans_triangle = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                triangle = [points[i], points[j], points[k]]
                if check_triangle_existance(triangle):
                    r = get_inner_circle_radius(triangle)
                    R = get_outer_circle_radius(triangle)
                    if R - r > max_diff:
                        max_diff = R - r
                        ans_triangle = triangle.copy()
                        radiuses = [r, R]
    if not ans_triangle:
        return []
    max_diff = pi * (radiuses[1] ** 2 - radiuses[0] ** 2)
    in_center = get_inner_circle_center(ans_triangle)
    out_center = get_outer_circle_center(ans_triangle)
    return [ans_triangle, max_diff, [in_center, radiuses[0]], [out_center, radiuses[1]]]

def get_inner_circle_center(points: list) -> list:
    P = get_triangle_half_perim(points) * 2
    x1 = points[0][0]
    x2 = points[1][0]
    x3 = points[2][0]
    y1 = points[0][1]
    y2 = points[1][1]
    y3 = points[2][1]
    a1 = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    a2 = sqrt((y3 - y2) ** 2 + (x3 - x2) ** 2)
    a3 = sqrt((y3 - y1) ** 2 + (x3 - x1) ** 2)
    
    x0 = (a2 * x1 + a3 * x2 + a1 * x3) / P
    y0 = (a2 * y1 + a3 * y2 + a1 * y3) / P

    return [x0, y0]

def get_outer_circle_center(points: list) -> list:
    x1 = points[0][0]
    x2 = points[1][0]
    x3 = points[2][0]
    y1 = points[0][1]
    y2 = points[1][1]
    y3 = points[2][1]

    D = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
    d = 2 * np.linalg.det(D)
    X = np.array([[x1 ** 2 + y1 ** 2, y1, 1], [x2 ** 2 + y2 ** 2, y2, 1], [x3 ** 2 + y3 ** 2, y3, 1]])
    Y = np.array([[x1 ** 2 + y1 ** 2, x1, 1], [x2 ** 2 + y2 ** 2, x2, 1], [x3 ** 2 + y3 ** 2, x3, 1]])

    x0 = np.linalg.det(X) / d
    y0 = -np.linalg.det(Y) / d

    return [x0, y0]

def main():
    # points = [(0, 0), (5, 0), (0, 8.66)]
    # points = [(0, 0), (5, 0), (0, 5)]
    points = [(0, 1e-5), (1e-5, 0), (0, 5e-5)]
    print(solve(points))


if __name__ == '__main__':
    main()
