from karel.stanfordkarel import *

def main():
    while left_is_clear():
        clean_beepers()
        move_down()
        move_up()
        turn_right()
    clean_beepers()

def clean_beepers():
    while front_is_clear():
        safe_pick_beeper()
        move()
    safe_pick_beeper()
  
def safe_pick_beeper():
    if beepers_present():
        pick_beeper()
      
def move_down():
    turn_left()
    turn_left()
    while front_is_clear():
        move()

def move_up():
    turn_right()
    move()
  
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
