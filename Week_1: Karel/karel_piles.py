# pick up all the beepers in the world.
from karel.stanfordkarel import *

def main():
    """Navigates through the world and picks up piles of 10 beepers each."""
    while front_is_clear():
        move()
        pick_pile()

def pick_pile():
    """Picks up a stack of exactly 10 beepers from the current corner."""
    for i in range(10):
        if beepers_present():
            pick_beeper()

if __name__ == '__main__':
    main()
