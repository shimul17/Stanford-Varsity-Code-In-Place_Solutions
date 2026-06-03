from karel.stanfordkarel import *

def main():  
    while beepers_present():
        follow_straight_trail()
        step_backwards()
        turn_left()
        move()
        if no_beepers_present():
            step_backwards()
            turn_around()
            move()
          
def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()
      
def step_backwards():
    turn_around()
    move()
    turn_around()
  
def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
