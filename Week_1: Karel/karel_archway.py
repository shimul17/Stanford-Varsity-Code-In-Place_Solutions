from karel.stanfordkarel import *

def main():
    """Karel climbs up, passes over, and safely climbs down an archway."""
    turn_left()
    for i in range(3):
        move()
    next_column()
    move_down()
    turn_left()

def next_column():
    """Moves Karel horizontally across the top section of the archway."""
    for i in range(3):
        turn_left()
    for i in range(3):
        move()

def move_down():
    """Brings Karel downward back to the surface level."""
    for i in range(3):
        turn_left()
    for i in range(3):
        move()

if __name__ == '__main__':
    main()
