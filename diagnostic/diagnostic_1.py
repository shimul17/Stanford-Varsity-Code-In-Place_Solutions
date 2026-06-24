def main():
    # Take height input from the user as a decimal number
    height = float(input("Enter astronaut height in cm: "))
    
    # Check if the height is between 160 cm and 190 cm
    if height >= 160 and height <= 190:
        print("The candidate is eligible to be an astronaut!")
    else:
        print("The candidate is NOT eligible due to height restrictions.")
        
if __name__ == "__main__":
    main()
