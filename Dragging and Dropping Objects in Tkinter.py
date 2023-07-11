from tkinter import *
from tkinter import messagebox


class DragDropLabel(object):
    def __init__(self, text):
        self.text = str(text)

        def labelpress(event):
            setattr(label, 'start_x', event.x)
            setattr(label, 'start_y', event.y)

        def labelmotion(event):
            # Calculate the distance moved by the mouse
            dx = event.x - getattr(label, 'start_x', 0)
            dy = event.y - getattr(label, 'start_y', 0)
            label.place(x=label.winfo_x() + dx, y=label.winfo_y() + dy)
            print(str(label.winfo_x())+" "+str(label.winfo_y()))
            canvas.create_line((0, 0, label.winfo_x(), label.winfo_y()), width=2, fill='blue')

        area = 4  # value must be even
        label = Label(canvas, text=self.text, bg="green", height=int(area / 2), width=area)
        label.place(x=5, y=5)
        label.bind("<ButtonPress-1>", labelpress)
        label.bind("<B1-Motion>", labelmotion)
        nodelist.append(label)


def spawn():
    if entrylist[0].get() == "" or entrylist[1].get() == "" or entrylist[2].get() == "":
        messagebox.showwarning("Missing Information")
    else:
        DragDropLabel(entrylist[0].get())
        DragDropLabel(entrylist[1].get())
        entrylist[2].get()
        for j in entrylist:
            j.delete(0, END)
    print("clicked")


nodelist = []
entrylist = []
x = 0
y = 0

root = Tk()
width = 1250
height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width - width) // 2
y_pos = ((screen_height - height) // 2) - 40
root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
root.config(bg="white")
root.maxsize(width=1250, height=750)
root.minsize(width=1250, height=750)

canvas = Canvas(root, width=1250, height=750)
canvas.config(bg="gray")
canvas.pack()

source = Label(canvas, text="Source", width=12)
source.place(x=1000, y=5)
destination = Label(canvas, text="Destination", width=12, height=1)
destination.place(x=1000, y=35)
weight = Label(canvas, text="Weight", width=12, height=1)
weight.place(x=1000, y=65)

for i in range(3):
    entry = Entry(canvas, width=12, font=("raleway", 11))
    entry.place(x=1100, y=5 + y)
    y += 30
    entrylist.append(entry)

spawnbutton = Button(canvas, text="Add Edge", command=spawn)
spawnbutton.place(x=1000, y=95)

root.mainloop()