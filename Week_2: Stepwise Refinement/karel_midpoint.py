from karel.stanfordkarel import *

"""
File: karel_midpoint.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint of the world and leave a beeper there.
"""

def main():
    """
    Finds the midpoint of the world by placing beepers at both ends
    and narrowing down the distance iteratively (ping-pong method).
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    
    # Move inward to start the ping-pong loop
    if front_is_clear():
        move()
        
    while no_beepers_present():
        while no_beepers_present():
            move()
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        move()
        
    # Align Karel exactly on the correct midpoint column
    align_karel_exactly_on_the_midpoint()

def align_karel_exactly_on_the_midpoint():
    """
    Adjusts Karel's position based on its facing direction to ensure 
    it stops exactly on the midpoint column and cleans up extra beepers.
    """
    if facing_east():
        pick_beeper()
        turn_around()
        move()
    else:
        turn_around()
        move()
        pick_beeper()
        turn_around()
        move()
        
    # Permanently face East as part of the post-condition
    while not_facing_east():
        turn_left()

def turn_around():
    """
    Turns Karel 180 degrees around.
    """
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
