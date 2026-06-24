import tkinter as tk

def main():
    # Draws two cars using Python's built-in tkinter
    root = tk.Tk()
    root.title("Draw Cars")
    
    # Create a 400x400 canvas (similar to Stanford Canvas)
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()
    x = 10
    y = 10
    draw_car(canvas, x, y)

    x = 100
    y = 100
    draw_car(canvas, x, y)

def draw_car(canvas, x, y):
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
