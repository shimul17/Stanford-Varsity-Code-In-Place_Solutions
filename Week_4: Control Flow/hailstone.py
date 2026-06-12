"""
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    n = int(input("Enter a number: "))
    # until n equal to 1 loop will continue
    while n != 1:
        # if n is even
        if n % 2 == 0:
            half = n // 2
            print(f"{n} is even, so I take half: {half}")
            n = half
        else:
            # if n is odd
            next_val = 3 * n + 1
            print(f"{n} is odd, so I make 3n + 1: {next_val}")
            n = next_val
          
if __name__ == "__main__":
    main()
