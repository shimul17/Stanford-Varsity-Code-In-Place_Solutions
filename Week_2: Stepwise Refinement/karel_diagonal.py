from karel.stanfordkarel import *

def main():
    # keep stepping up until the top
    while front_is_clear():
        # Assume: Karel is facing right (east) 
        put_beeper()
        turn_left()
        move()
        turn_right()
        move()
    put_beeper()
    
def turn_right():
    # defines turn_right as 3x turn_left
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()


