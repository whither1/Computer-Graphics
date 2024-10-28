import math as m

def get_four_point(center, point):
    cx, cy = center[0], center[1]
    px, py = point[0], point[1]
    dx, dy = px - cx, py - cy
    return [cx + dx, cy + dy], [cx + dx, cy - dy], [cx - dx, cy + dy], [cx - dx, cy - dy]

def get_eight_point(center, point):
    cx, cy = center[0], center[1]
    px, py = point[0], point[1]
    dx, dy = px - cx, py - cy
    if (cx < 0 and cy < 0) or (cx > 0 and cy > 0):
        return ([cx + dx, cy + dy], [cx + dx, cy - dy], [cx - dx, cy + dy], [cx - dx, cy - dy],
                [cy + dy, cx + dx], [cy - dy, cx + dx], [cy + dy, cx - dx], [cy - dy, cx - dx])
    else:
        return ([cx + dx, cy + dy], [cx + dx, cy - dy], [cx - dx, cy + dy], [cx - dx, cy - dy],
                [-(cy + dy), -(cx + dx)], [-(cy - dy), -(cx + dx)], [-(cy + dy), -(cx - dx)], [-(cy - dy), -(cx - dx)])

def canonic_circle(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r = round(data[1][0])
    b = round(x0 + r / m.sqrt(2))
    r_2 = r ** 2

    for x in range(x0, b + 1):
        y = round(y0 + m.sqrt(r_2 - (x - x0) ** 2))
        tmp = get_eight_point([x0, y0], [x, y])
        for i in range(8):
            arr.append(tmp[i])

    return arr

def canonic_ellipse(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r_x = round(data[1][0])
    r_y = round(data[1][1])
    a_sq = r_x * r_x
    b_sq = r_y * r_y

    b_x = a_sq / (m.sqrt(a_sq + b_sq))  # выведено из равенства производной уравнения эллипса единице
    b_y = b_sq / (m.sqrt(a_sq + b_sq))

    for x in range(0, round(b_x) + 1):
        y = round(m.sqrt((a_sq * b_sq - b_sq * x * x) / a_sq)) + y0
        tmp = get_four_point([x0, y0], [x + x0, y])
        for i in range(4):
            arr.append(tmp[i])

    for y in range(0, round(b_y) + 1):
        x = round(m.sqrt((a_sq * b_sq - a_sq * y * y) / b_sq)) + x0
        tmp = get_four_point([x0, y0], [x, y + y0])
        for i in range(4):
            arr.append(tmp[i])

    return arr

def param_circle(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r = round(data[1][0])

    inc_angle = 1 / r
    angle = m.pi / 2
    while angle > m.pi / 4:
        x = round(m.cos(angle) * r + x0)
        y = round(m.sin(angle) * r + y0)
        tmp = get_eight_point([x0, y0], [x, y])
        for i in range(8):
            arr.append(tmp[i])
        angle -= inc_angle
    return arr

def param_ellipse(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r_x = round(data[1][0])
    r_y = round(data[1][1])
    step = 1 / r_x
    if r_y > r_x:
        step = 1 / r_y

    i = 0
    while i <= m.pi / 2 + step:
        x = round(x0 + r_x * m.cos(i))
        y = round(y0 + r_y * m.sin(i))
        tmp = get_four_point([x0, y0], [x, y])
        for j in range(4):
            arr.append(tmp[j])
        i += step
    return arr

def bres_circle(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r = round(data[1][0])
    x = 0
    y = r
    # delta = (xi + 1) ^ 2 + (yi - 1) ^ 2 - R ^ 2
    delta = 2 * (1 - r)
    tmp = get_eight_point([x0, y0], [x0, y0 + r])
    for i in range(8):
        arr.append(tmp[i])
    # Работаем только в верхней восьмой части (верхняя половина первой четверти)
    # Поэтому можно не добавлять третий случай в if когда меняется только y
    while x < y:
        d = 2 * delta + 2 * y - 1
        x += 1
        if d < 0:
            delta += 2 * x + 1
        else:
            y -= 1
            delta += 2 * (x - y + 1)
        tmp = get_eight_point([x0, y0], [x + x0, y + y0])
        for i in range(8):
            arr.append(tmp[i])
    return arr

def bres_ellipse(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r_x = round(data[1][0])
    r_y = round(data[1][1])
    r_x_q = r_x * r_x
    r_y_q = r_y * r_y

    # начинаем работу алгоритма с верхней точки окружности
    # x, y - координаты точки в осях связанных с центром окружности, далее корректируем это где нужно
    x = 0
    y = r_y
    # delta = b ^ 2 * (xi + 1) ^ 2 + r_x ^ 2 * (yi - 1) ^ 2 - (r_x * b) ^ 2
    # delta_start = b ^ 2 + (r_x * b) ^ 2 - 2 * b * r_x ^ 2 + r_x ^ 2 - (r_x * b) ^ 2 = r_x ^ 2 + b ^ 2 - 2 * b * r_x ^ 2
    delta = r_x_q + r_y_q - 2 * r_y * r_x_q
    tmp = get_four_point([x0, y0], [x, y0 + r_y])
    for j in range(4):
        arr.append(tmp[j])
    # Работаем только в верхней правой четверти
    while y >= 0:
        # Точно диагональный шаг
        if delta == 0:
            x += 1
            y -= 1
            delta += (2 * x + 1) * r_y_q + (1 - 2 * y) * r_x_q
        # Горизонтальный или диагональный
        elif delta < 0:
            d = 2 * delta + (2 * y - 1) * r_x_q
            # Горизонтальный шаг
            if d <= 0:
                x += 1
                delta += (2 * x + 1) * r_y_q
            # Диагональный шаг
            else:
                x += 1
                y -= 1
                delta += (2 * x + 1) * r_y_q + (1 - 2 * y) * r_x_q
            #delta += (2 * x + 1) * b_sq
        # Вертикальный или диагональный
        else:
            d = 2 * delta + (- 2 * x - 1) * r_y_q
            # Диагональный
            if d <= 0:
                x += 1
                y -= 1
                delta += (2 * x + 1) * r_y_q + (1 - 2 * y) * r_x_q
            # Вертикальный
            else:
                y -= 1
                delta += (-2 * y + 1) * r_x_q

        tmp = get_four_point([x0, y0], [x + x0, y + y0])
        for j in range(4):
            arr.append(tmp[j])
    return arr

def middle_point_circle(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r = round(data[1][0])

    a_2 = r * r
    da_2 = 2 * a_2
    x = 0
    y = r

    # граница инкрементации по x и по y
    border_x = a_2 / (m.sqrt(a_2 + a_2))  # выведено из равенства производной уравнения эллипса единице

    # начальное значение пробной функции fi = b^2 * (xi-1 + 1)^2 + a^2 * (yi-1 - 1/2)^2 - (a * b)^2
    # f0 = b^2 + a^2 * (b^2 - b + 1/4) - (a * b) ^ 2 = b^2 - a^2 * b + a^2 / 4
    f = a_2 + a_2 / 4 - a_2 * r

    for i in range(0, round(border_x)):
        tmp = get_eight_point([x0, y0], [x + x0, y + y0])
        for j in range(8):
            arr.append(tmp[j])
        x += 1
        if f <= 0:
            f += da_2 * x + a_2
        else:
            y -= 1
            f += da_2 * x + a_2 - 2 * a_2 * y
    return arr


def middle_point_ellipse(data):
    arr = []
    x0 = round(data[0][0])
    y0 = round(data[0][1])
    r_x = round(data[1][0])
    r_y = round(data[1][1])

    a_2 = r_x * r_x
    b_2 = r_y * r_y

    da_2 = -2 * a_2
    db_2 = 2 * a_2

    x = 0
    y = r_y

    # граница инкрементации по x и по y
    border_x = a_2 / (m.sqrt(a_2 + b_2))  # выведено из равенства производной уравнения эллипса единице
    border_y = b_2 / (m.sqrt(a_2 + b_2))

    # начальное значение пробной функции fi = b^2 * (xi-1 + 1)^2 + a^2 * (yi-1 - 1/2)^2 - (a * b)^2
    # f0 = b^2 + a^2 * (b^2 - b + 1/4) - (a * b) ^ 2 = b^2 - a^2 * b + a^2 / 4
    f = b_2 + a_2 / 4 - a_2 * r_y

    for i in range(0, round(border_x)):
        tmp = get_four_point([x0, y0], [x + x0, y + y0])
        for j in range(4):
            arr.append(tmp[j])
        x += 1
        if f <= 0:
            f += db_2 * x + b_2
        else:
            y -= 1
            f += db_2 * x + b_2 + da_2 * y

    # для перехода в центральной точке меняем f
    f += -(a_2 * y + b_2 * x) + 3 * (a_2 - b_2) / 4

    for i in range(round(border_y), -1, -1):
        tmp = get_four_point([x0, y0], [x + x0, y + y0])
        for j in range(4):
            arr.append(tmp[j])
        y -= 1
        if f >= 0:
            f += da_2 * y + a_2
        else:
            x += 1
            f += da_2 * y + a_2 + 2 * b_2 * x
    return arr