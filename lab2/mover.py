from math import sin, cos, pi

def move(state, center, dx, dy):
    center[0] += dx
    center[1] += dy
    for line in state['lines']:
        line[0][0] += dx
        line[0][1] += dy
        line[1][0] += dx
        line[1][1] += dy
    for circle in state['circles']:
        for point in circle:
            point[0] += dx
            point[1] += dy
    return state, center

def rotate(state, center, angle, fig_center):
    rads = pi / 180
    for line in state['lines']:
        x0 = line[0][0]
        line[0][0] = (x0 - center[0]) * cos(angle * rads) - (line[0][1] - center[1]) * sin(angle * rads) + center[0]
        line[0][1] = (x0 - center[0]) * sin(angle * rads) + (line[0][1] - center[1]) * cos(angle * rads) + center[1]
        x0 = line[1][0]
        line[1][0] = (x0 - center[0]) * cos(angle * rads) - (line[1][1] - center[1]) * sin(angle * rads) + center[0]
        line[1][1] = (x0 - center[0]) * sin(angle * rads) + (line[1][1] - center[1]) * cos(angle * rads) + center[1]
    for circle in state['circles']:
        for point in circle:
            x0 = point[0]
            point[0] = (x0 - center[0]) * cos(angle * rads) - (point[1] - center[1]) * sin(angle * rads) + center[0]
            point[1] = (x0 - center[0]) * sin(angle * rads) + (point[1] - center[1]) * cos(angle * rads) + center[1]
    x0 = fig_center[0]
    fig_center[0] = (x0 - center[0]) * cos(angle * rads) - (fig_center[1] - center[1]) * sin(angle * rads) + center[0]
    fig_center[1] = (x0 - center[0]) * sin(angle * rads) + (fig_center[1] - center[1]) * cos(angle * rads) + center[1]

    return state, fig_center

def scale(state, center, kx, ky, fig_center):
    for line in state['lines']:
        line[0][0] = (line[0][0] - center[0]) * kx + center[0]
        line[0][1] = (line[0][1] - center[1]) * ky + center[1]
        line[1][0] = (line[1][0] - center[0]) * kx + center[0]
        line[1][1] = (line[1][1] - center[1]) * ky + center[1]
    for circle in state['circles']:
        for point in circle:
            point[0] = (point[0] - center[0]) * kx + center[0]
            point[1] = (point[1] - center[1]) * ky + center[1]
    fig_center[0] = (fig_center[0] - center[0]) * kx + center[0]
    fig_center[1] = (fig_center[1] - center[1]) * ky + center[1]

    return state, fig_center
