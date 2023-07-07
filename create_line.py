import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# List of points defining the line
points = [50, 50, 150, 150, 250, 100, 350, 200]

# Draw a line using the list of points
#                   points
canvas.create_line((50,50,100,100), width=2, fill='blue')

root.mainloop()
