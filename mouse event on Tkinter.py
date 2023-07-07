import tkinter as tk

root = tk.Tk()

# Create a widget
widget = tk.Label(root, text="Hello, World!")
widget.pack()

# Get the width and height of the widget
width = widget.winfo_width()
height = widget.winfo_height()

print("Width:", width)
print("Height:", height)

root.mainloop()
