from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    """
    Main function to execute the checkerboard pattern.
    Fills the first row, moves through the remaining rows,
    and then returns Karel back to the starting position.
    """
    put_beeper()
    
    # Step 2: Fill the entire first row in checkerboard style
    fill_row()
    
    # Step 3: Fill all the remaining rows one by one in an alternating pattern
    while left_is_clear():
        move_up_to_next_row()
        fill_row()
        
    # Step 4: Return Karel exactly to the initial position (1, 1) facing East upon completion
    universal_return_to_start()

def fill_row():
    # If the path ahead is clear, move two spaces and place a beeper every alternate corner
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def move_up_to_next_row():
    if facing_east():
        turn_left()
        if beepers_present():
            # Check if the upper row exists before moving
            if front_is_clear(): 
                move()
                turn_left()
                # Check if the next space is clear before moving left
                if front_is_clear(): 
                    move()
                    put_beeper()
        else:
            if front_is_clear():
                move()
                turn_left()
                put_beeper()
    else:
        turn_right()
        if beepers_present():
          # Check if the upper row exists before moving  
          if front_is_clear(): 
                move()
                turn_right()
                # Check if the next space is clear before moving right
                if front_is_clear(): 
                    move()
                    put_beeper()
        else:
            if front_is_clear():
                move()
                turn_right()
                put_beeper()

def universal_return_to_start():
    # 1. First, face Karel directly South
    while not_facing_south():
        turn_left()
        
    # 2. Move straight down to the first row (Row 1)
    while front_is_clear():
        move()
        
    # 3. Now, face Karel West
    while not_facing_west():
        turn_left()
        
    # 4. Move straight left to the first column (Column 1)
    while front_is_clear():
        move()
        
    # 5. Finally, face Karel East according to the initial starting condition
    while not_facing_east():
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
