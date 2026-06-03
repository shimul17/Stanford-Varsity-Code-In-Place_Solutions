from karel.stanfordkarel import *

def main():
    """Karel jumps over 3 obstacles and places a beeper after each."""
    move()
    for i in range(3):
        jump_obstacle()
        put_beeper()
    move()
    move()

def jump_obstacle():
    """Navigates Karel safely over a single obstacle block."""
    turn_left()
    move()
    for i in range(2):
        turn_right()
        move()
    turn_left()

def turn_right():
    """Turns Karel 90 degrees to the right."""
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
