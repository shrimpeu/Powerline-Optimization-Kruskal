import tkinter as tk


def create_circle_label(root, radius, color, text):
    canvas = tk.Canvas(root, width=2 * radius, height=2 * radius, bg=color, highlightthickness=0)
    canvas.create_oval(0, 0, 2 * radius, 2 * radius, fill=color)
    canvas.create_text(radius, radius, text=text, fill="white")
    canvas.pack()


root = tk.Tk()
create_circle_label(root, radius=50, color="blue", text="Circle Label")
root.mainloop()