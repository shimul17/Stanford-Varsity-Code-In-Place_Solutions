from karel.stanfordkarel import *

def main():
    """
    Fills the whole world with beepers.
    Pre: Karel starts at the bottom-left corner facing East.
    Post: The entire world is filled with beepers.
    """
    while left_is_clear():
        build_row()
        next_row()
    build_row()
  
def build_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
  
def next_row():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
  
def turn_right():
    for i in range(3):
        turn_left()
        
if __name__ == '__main__':
    main()
