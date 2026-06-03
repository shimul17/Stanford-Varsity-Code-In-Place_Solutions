from karel.stanfordkarel import *

def main():
    while front_is_clear():
            move()
            if front_is_blocked():
               find_next_path()
    turn_left()
def find_next_path():
    
    turn_left()
    if front_is_blocked():
        turn_around()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
