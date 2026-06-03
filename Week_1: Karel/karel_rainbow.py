from karel.stanfordkarel import *

def main():
    """Karel moves forward while painting the ground with rainbow colors."""
    paint_corner('red')
    move()
    paint_corner('orange')
    move()
    paint_corner('yellow')
    move()
    paint_corner('green')
    move()
    paint_corner('blue')
    move()

if __name__ == '__main__':
    main()
