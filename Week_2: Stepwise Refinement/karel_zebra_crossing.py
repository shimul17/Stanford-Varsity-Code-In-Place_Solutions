from karel.stanfordkarel import *

def main():
    draw_stripe()
    while front_is_clear():
        for i in range(4):
            move()
        draw_stripe()
def draw_stripe():
    # 1st column
    turn_left()
    beeper_column()
    # move to next column
    turn_right()
    move()
    # 2nd column
    turn_right()
    beeper_column()
    # for face to next column
    turn_left()
def beeper_column():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
def turn_right():
    for i in range(3):
        turn_left()
 
if __name__ == '__main__':
    main()
