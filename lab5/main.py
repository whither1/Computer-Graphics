import tkinter as tk
from tkinter import colorchooser
import util
import fill


class RootWindow(tk.Tk):
    """
        Representation of root program window.
    """

    color = "#000000"
    edges = [[]]
    active_edges = []
    y_groups = []
    y_max = 0
    y_min = 1000
    x_avg = 0

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        img = tk.PhotoImage(file="~/CompGraph/lab5/icon.png")

        self.geometry("1910x1000+0+0")
        self.minsize(1, 1)
        self.maxsize(1920, 1010)
        self.resizable(0, 0)
        self.title("Filling with sorted edges")
        self.iconphoto(True, img)
        self.configure(
            background="#000080",
            highlightcolor="black"
        )

        self.image = tk.PhotoImage(width=1290, height=954)
        self.image.put("#FFFFFF", to=(0, 0, 1290, 954))
        self.canvas = tk.Canvas(self)
        self.canvas.place(relx=0.307, rely=0.028, relheight=0.945, relwidth=0.677)
        self.canvas.configure(
            background="#ffffff",
            borderwidth="2",
            relief="ridge",
            selectbackground="#c4c4c4"
        )
        self.canvas.create_image((645, 477), image=self.image, state="normal")
        self.canvas.bind("<Button-1>", lambda event: self.pixclick(event))
        self.canvas.bind("<Button-3>", lambda event: self.pixclose(event))

        # Mode selection section.
        self.modelb = tk.Label(self)
        self.modelb.place(relx=0.031, rely=0.028, height=58, width=476)
        self.modelb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="РЕЖИМ"
        )

        self.modelst = tk.Listbox(self, exportselection=0)
        self.modelst.place(relx=0.031, rely=0.083, relheight=0.065, relwidth=0.25)
        self.modelst.configure(
            background="white",
            foreground="black",
            selectbackground="#000080",
            selectforeground="white",
            font="-family {Consolas} -size 14"
        )
        self.modelst.insert(tk.END, "Без задержки")
        self.modelst.insert(tk.END, "С задержкой")

        # Color selection section.
        self.colorlb = tk.Label(self)
        self.colorlb.place(relx=0.031, rely=0.168, height=56, width=476)
        self.colorlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="ЦВЕТ"
        )

        self.colorpicker = tk.Button(self)
        self.colorpicker.place(relx=0.031, rely=0.218, height=42, width=476)
        self.colorpicker.configure(
            background="black",
            activebackground="black",
            font="-family {Consolas} -size 14",
            command=lambda: self.get_color()
        )

        # New dot section.
        self.dotlb = tk.Label(self)
        self.dotlb.place(relx=0.031, rely=0.278, height=56, width=476)
        self.dotlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 18",
            foreground="#ffffff",
            text="КООРДИНАТЫ ТОЧКИ"
        )

        self.xlb = tk.Label(self)
        self.xlb.place(relx=0.031, rely=0.327, height=33, width=232)
        self.xlb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="X"
        )

        self.ylb = tk.Label(self)
        self.ylb.place(relx=0.157, rely=0.327, height=33, width=232)
        self.ylb.configure(
            activebackground="#000080",
            activeforeground="white",
            background="#000080",
            font="-family {Consolas} -size 14",
            foreground="#ffffff",
            text="Y"
        )

        self.xsb = tk.Spinbox(self)
        self.xsb.place(relx=0.031, rely=0.357, relheight=0.039, relwidth=0.125)
        self.xsb.configure(
            activebackground="#f9f9f9",
            background="white",
            foreground="black",
            buttonbackground="#d9d9d9",
            justify="center",
            font="-family {Consolas} -size 14",
            highlightbackground="black",
            relief="flat",
            selectbackground="#c4c4c4",
            from_=0.0,
            to=1300.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.ysb = tk.Spinbox(self)
        self.ysb.place(relx=0.1553, rely=0.357, relheight=0.039, relwidth=0.125)
        self.ysb.configure(
            activebackground="#f9f9f9",
            background="white",
            foreground="black",
            buttonbackground="#d9d9d9",
            justify="center",
            font="-family {Consolas} -size 14",
            highlightbackground="black",
            relief="flat",
            selectbackground="#c4c4c4",
            from_=0.0,
            to=1300.0,
            increment=1.0,
            textvariable=tk.IntVar()
        )

        self.addbtn = tk.Button(self)
        self.addbtn.place(relx=0.031, rely=0.396, height=42, width=477)
        self.addbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Добавить точку",
            command=self.add_dot
        )

        self.fillbtn = tk.Button(self)
        self.fillbtn.place(relx=0.031, rely=0.803, height=41, width=476)
        self.fillbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Выполнить закраску",
            command=lambda: fill.fill(ROOT)
        )

        self.timebtn = tk.Button(self)
        self.timebtn.place(relx=0.031, rely=0.861, height=40, width=476)
        self.timebtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Замерить время",
            command=lambda: util.measure_time(ROOT)
        )

        self.clrbtn = tk.Button(self)
        self.clrbtn.place(relx=0.031, rely=0.917, height=41, width=476)
        self.clrbtn.configure(
            background="#d9d9d9",
            foreground="black",
            activebackground="#000080",
            font="-family {Consolas} -size 14",
            text="Очистить экран",
            command=self.reset_img
        )

    def reset_img(self):
        self.image.put("#FFFFFF", to=(0, 0, 1290, 954))
        self.edges = [[]]
        self.active_edges = []
        self.y_groups = []
        self.y_max = 0
        self.y_min = 1000
        self.x_avg = 0

    def get_color(self):
        _, hex_code = colorchooser.askcolor(
            parent=self,
            title="Выберите цвет для закрашивания",
            initialcolor=self.color
        )
        self.colorpicker.configure(
            background=hex_code,
            activebackground=hex_code
        )
        self.color = hex_code

    def update_y_group(self, x_start, y_start, x_end, y_end):
        if y_start > y_end:
            x_end, x_start = x_start, x_end
            y_end, y_start = y_start, y_end

        if y_end > self.y_max:
            self.y_max = y_end

        if y_start < self.y_min:
            self.y_min = y_start

        y_proj = y_end - y_start if y_end - y_start else 1
        x_step = -(x_end - x_start) / y_proj
        if y_proj != 1:
            self.y_groups.append([x_start, x_step, y_end, y_start])
        
        self.x_avg += x_start

    def pixclick(self, event):
        self.edges[-1].extend([[event.x, event.y, self.color]])
        if len(self.edges[-1]) > 1:
            line = util.bresenham_int(
                self.edges[-1][-2][0],
                self.edges[-1][-2][1],
                self.edges[-1][-1][0],
                self.edges[-1][-1][1],
                self.color
            )
            util.draw_line(self.image, line)
            self.update_y_group(
                self.edges[-1][-2][0],
                self.edges[-1][-2][1],
                self.edges[-1][-1][0],
                self.edges[-1][-1][1]
            )
        print(self.y_groups)

    def pixclose(self, event):
        if len(self.edges[-1]) > 1:
            line = util.bresenham_int(
                self.edges[-1][0][0],
                self.edges[-1][0][1],
                self.edges[-1][-1][0],
                self.edges[-1][-1][1],
                self.color
            )
            util.draw_line(self.image, line)
            self.update_y_group(
                self.edges[-1][0][0],
                self.edges[-1][0][1],
                self.edges[-1][-1][0],
                self.edges[-1][-1][1]
            )
            self.edges.append([])
        print(self.y_groups)

    def add_dot(self):
        x = int(self.xsb.get())
        y = int(self.ysb.get())
        self.edges[-1].extend([[x, y, self.color]])
        if len(self.edges[-1]) > 1:
            line = util.bresenham_int(
                self.edges[-1][-2][0],
                self.edges[-1][-2][1],
                self.edges[-1][-1][0],
                self.edges[-1][-1][1],
                self.color
            )
            util.draw_line(self.image, line)
            self.update_y_group(
                self.edges[-1][-2][0],
                self.edges[-1][-2][1],
                self.edges[-1][-1][0],
                self.edges[-1][-1][1]
            )
        print(self.y_groups)


if __name__ == "__main__":
    ROOT = RootWindow()
    ROOT.mainloop()
