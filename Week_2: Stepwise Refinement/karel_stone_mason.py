from karel.stanfordkarel import *

"""
Karel should have repaired each of the columns in the temple
"""

def main():
    for i in range(3):
        build_column()
        move_to_next_column()
    # Fencepost problem: build the final column
    build_column()

def build_column():
    """
    Builds a single column upwards and returns to the bottom.
    """
    turn_left()
    # Assuming columns are 4 spaces high (adjust range if needed)
    for i in range(4):
        if no_beepers_present():
            put_beeper()
        move()
    # Put the final beeper at the top if missing
    if no_beepers_present():
        put_beeper()
    return_to_bottom()

def return_to_bottom():
    turn_around()
    while front_is_clear():
        move()
    turn_left() # Face East again

def move_to_next_column():
    # Move 4 steps to the next column position
    for i in range(4):
        move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
