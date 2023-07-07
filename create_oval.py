import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Create a circle with a larger size
x = 200  # x-coordinate of the circle's center
y = 200  # y-coordinate of the circle's center
radius = 100  # radius of the circle
canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='blue')

# to configure a create_oval()
circle_id = canvas.create_oval(x+100 - radius, y+100 - radius, x+100 + radius, y+100 + radius, fill="blue")
canvas.itemconfig(circle_id, fill="red")


root.mainloop()
