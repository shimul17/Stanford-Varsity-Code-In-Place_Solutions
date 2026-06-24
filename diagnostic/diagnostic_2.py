# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    # Loop through numbers from 1 up to MAX_NUMBER (inclusive)
    for i in range(1, MAX_NUMBER + 1):
        # Check if the number is even
        if i % 2 == 0:
            print(f"{i} is even")
        # If the number is not even, it must be odd
        else:
            print(f"{i} is odd")

if __name__ == "__main__":
    main()
