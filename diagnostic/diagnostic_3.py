def main():
    print("Enter a sequence of non-decreasing numbers.")
    
    # Take the first number from the user
    current_num = float(input("Enter number: "))
    count = 1  # Track how many numbers have been successfully entered
    
    while True:
        # Take the next number for comparison
        next_num = float(input("Enter number: "))
        
        # Check if the sequence breaks (if the new number is smaller)
        if next_num < current_num:
            print("Thanks for playing!")
            print(f"Sequence length: {count}")
            break  # Exit the loop immediately
        
        # Update the current number and increase the count
        current_num = next_num
        count += 1

if __name__ == "__main__":
    main()
