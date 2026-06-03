from karel.stanfordkarel import *

def main():
    """
    Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
    Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
    """
    for i in range(2):
        move_to_wall()
        bloom_flower()
    move_to_wall()
  
def bloom_flower():
    climb_stem()
    make_bloom()
    move_to_wall()
    turn_left()
  
def climb_stem():
    turn_left()
    while right_is_blocked():
        move()
      
def make_bloom():
    # Makes a square of beepers
    put_beeper()
    move()
    for i in range(2):
        put_beeper()
        turn_right()
        move()
    put_beeper()

def move_to_wall():
    # Karel moves until blocked.
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
