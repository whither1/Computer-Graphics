import time
import util

def get_line(x_start, x_end, y, color):
    dots = []
    for x in range(x_end - x_start):
        dots.append([x_start + x, y, color])
    return dots

def draw_scanline(root, y_end, y_start, x_border, edge, delay):
    x_cur = edge[0]
    for y in range(y_start, y_end):
        if x_cur < x_border:
            line = get_line(round(x_cur), x_border, y, root.color)
            util.draw_line(root.image, line)
        elif x_cur > x_border:
            line = get_line(x_border, round(x_cur), y, root.color)
            util.draw_line(root.image, line)
        x_cur -= edge[1]
        if delay:
            time.sleep(0.01)
            root.canvas.update()

def fill(root):
    delay = root.modelst.get(root.modelst.curselection()[0])
    x_border = root.x_avg // len(root.y_groups)
    if delay == "С задержкой":
        delay = True
    else:
        delay = False
    # while y_end > y_start:
    for edge in root.y_groups:
        y_end = edge[2]
        y_start = edge[3]
        # check_active_edges(root.active_edges)
        # add_active_edges(root.y_groups, root.active_edges, y_end)
        draw_scanline(root, y_end, y_start, x_border, edge, delay)
