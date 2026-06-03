from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    
    while front_is_clear():
        place_zigzag_pair()
def place_zigzag_pair():
    put_beeper()
    move()
    turn_left()
    move()
    put_beeper()
    turn_around()
    move()
    turn_left()
    if front_is_clear():
        move()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()
