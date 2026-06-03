karel_basic.py
from karel.stanfordkarel import *

def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()

def turn_right():
    """Turns Karel 90 degrees to the right."""
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
