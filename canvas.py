import tkinter as tk
from tkinter import colorchooser

def draw(event):
    if tool == "pen":
        x1, y1 = event.x - 2, event.y - 2
        x2, y2 = event.x + 2, event.y + 2
        canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def change_color():
    global color
    color = colorchooser.askcolor(color=color)[1]

def clear_canvas():
    canvas.delete("all")

def set_tool_pen():
    global tool
    tool = "pen"

def set_tool_rectangle():
    global tool
    tool = "rectangle"

def set_tool_oval():
    global tool
    tool = "oval"

def start_draw(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def end_draw(event):
    if tool == "rectangle":
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline=color, fill=color)
    elif tool == "oval":
        canvas.create_oval(start_x, start_y, event.x, event.y, outline=color, fill=color)

tool = "pen"
color = "black"

root = tk.Tk()
root.title("Basic Paint App")
root.geometry("800x600")

canvas = tk.Canvas(root, bg="white", width=800, height=500)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonPress-1>", start_draw)
canvas.bind("<ButtonRelease-1>", end_draw)

btn_frame = tk.Frame(root)
btn_frame.pack(fill=tk.X, expand=True)

btns = [
    ("Pen", set_tool_pen),
    ("Rectangle", set_tool_rectangle),
    ("Oval", set_tool_oval),
    ("Change Color", change_color),
    ("Clear", clear_canvas)
]

for text, command in btns:
    tk.Button(btn_frame, text=text, command=command).pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.W)

root.mainloop()