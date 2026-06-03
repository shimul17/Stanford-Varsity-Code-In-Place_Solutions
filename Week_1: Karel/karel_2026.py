from karel.stanfordkarel import *

def main():
    """
    Karel places a pile of 20 beepers, moves forward, 
    and then places another pile of 26 beepers.
    """
    for i in range(20):
        put_beeper()
    move()
    for i in range(26):
        put_beeper()
    move()    

if __name__ == '__main__':
    main()
