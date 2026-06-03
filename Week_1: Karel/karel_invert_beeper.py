from karel.stanfordkarel import *

def main():
    # invert beeper on each corner in the row
    while front_is_clear():
        invert_beeper()
        move()
    # fence-post bug correction
    invert_beeper()

def invert_beeper():
    """ flips whether or not there is a beeper """
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

if __name__ == '__main__':
    main()
