import numpy as np

def cda_a(x1, y1, x2, y2):
    arr = []
    steps = 1
    dx, dy = x2 - x1, y2 - y1
    x, y = round(x1), round(y1)
    if int(abs(dx)) == 0 and int(abs(dy)) == 0:
        arr.append([round(x), round(y)])
        steps = 1
        return arr, steps
    if abs(dx) >= abs(dy):
        swap = 1
        l = abs(dx)
    else:
        swap = 0
        l = abs(dy)
    dx, dy = dx / l, dy / l
    for i in range(0, int(l) + 1):
        arr.append([round(x), round(y)])
        if swap and round(abs(y + dy)) > round(abs(y)):
            steps += 1
        elif not swap and round(abs(x + dx)) > round(abs(x)):
            steps += 1
        x += dx
        y += dy
    return arr, steps

def bres_float_a(x1, y1, x2, y2):
    arr = []
    steps = 1
    dx, dy = x2 - x1, y2 - y1
    x, y = round(x1), round(y1)
    sx, sy = int(np.sign(dx)), int(np.sign(dy))
    dx, dy = abs(dx), abs(dy)
    if int(dx) == 0 and int(dy) == 0:
        arr.append([x, y])
        steps = 1
        return arr, steps
    swap = 0
    if dx < dy:
        swap = 1
        dx, dy = dy, dx
    m = dy / dx
    e = m - 0.5
    i = 0
    while i < dx:
        arr.append([x, y])
        if e >= 0:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= 1
            steps += 1
        if swap == 0:
            x += sx
        else:
            y += sy
        e += m
        i += 1
    return arr, steps

def bres_int_a(x1, y1, x2, y2):
    arr = []
    steps = 1
    dx, dy = x2 - x1, y2 - y1
    x, y = round(x1), round(y1)
    sx, sy = int(np.sign(dx)), int(np.sign(dy))
    dx, dy = abs(dx), abs(dy)
    if int(dx) == 0 and int(dy) == 0:
        arr.append([x, y])
        steps = 1
        return arr, steps
    swap = 0
    if dx < dy:
        swap = 1
        dx, dy = dy, dx
    e = 2 * dy - dx
    dx2 = 2 * dx
    dy2 = 2 * dy
    for i in range(0, int(dx) + 1):
        arr.append([x, y])
        if e >= 0:
            if swap == 0:
                y += sy
            else:
                x += sx
            e -= dx2
            steps += 1
        if swap == 0:
            x += sx
        else:
            y += sy
        e += dy2
    return arr, steps


def bres_anti_a(x1, y1, x2, y2):
    arr = []
    steps = 1
    dx, dy = x2 - x1, y2 - y1
    sx, sy = int(np.sign(dx)), int(np.sign(dy))
    dx, dy = abs(dx), abs(dy)
    swap = 0
    if dx < dy:
        swap = 1
        dx, dy = dy, dx
    Imax = 1
    x, y = round(x1), round(y1)
    if int(dx) == 0 and int(dy) == 0:
        arr.append([x, y])
        steps = 1
        return arr, steps
    m = Imax * dy / dx
    w = Imax - m
    e = Imax / 2
    arr.append([x, y, m / 2])
    i = 0
    while i < dx + 1:
        if e <= w:
            if swap:
                y += sy
            else:
                x += sx
            e += m
        else:
            x += sx
            y += sy
            e -= w
            steps += 1
        arr.append([x, y, Imax - e])
        i += 1
    return arr, steps

def wu_a(x1, y1, x2, y2):
    arr = []
    steps = 1
    dx, dy = x2 - x1, y2 - y1
    sx, sy = int(np.sign(dx)), int(np.sign(dy))
    dx, dy = abs(dx), abs(dy)
    swap = 0
    if dx < dy:
        swap = 1
        dx, dy = dy, dx
        sx, sy = sy, sx
    if swap == 1:
        x, y = round(y1), round(x1)
    else:
        x, y = round(x1), round(y1)
    if int(dx) == 0 and int(dy) == 0:
        arr.append([x, y])
        steps = 1
        return arr, steps
    m = dy / dx
    i = 0
    while i < dx + 1:
        tmp_y, tmp_x = round(y), round(x)
        if swap == 1:
            arr.append([tmp_y, tmp_x, 1 - (y - tmp_y)])
            arr.append([tmp_y + 1, tmp_x, y - tmp_y])
        else:
            arr.append([tmp_x, tmp_y, 1 - (y - tmp_y)])
            arr.append([tmp_x, tmp_y + 1, y - tmp_y])
        if round(y + m) > round(y):
            steps += 1
        x += sx
        y += sy * m
        i += 1
    return arr, steps