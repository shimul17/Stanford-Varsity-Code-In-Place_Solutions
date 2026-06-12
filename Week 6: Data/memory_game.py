import random

NUM_PAIRS = 3
def get_valid_index(displayed, first_index=None):
    while True:
        user_input = input("Enter an index: ")
        if not user_input.isdigit():
            print("Not a number. Try again.")
            continue
        index = int(user_input)
        if index < 0 or index >= len(displayed):
            print("Invalid index. Try again.")
            continue
        if first_index is not None and index == first_index:
            print("You entered the same index twice. Try again.")
            continue
        if displayed[index] != '*':
            print("This number has already been matched. Try again.")
            continue 
        return index   

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    # empty list
    truth = []
    # for loop from 0 to -1 of Num_pairs
    for i in range(NUM_PAIRS):
    # to add every number twice
        truth.append(i)
        truth.append(i)
      
    # to do randomly order of list: random.shuffle 
    random.shuffle(truth)
   
    displayed = ['*'] * len(truth)
    
    while '*' in displayed:
        print(displayed)
    
        index1 = get_valid_index(displayed)
        index2 = get_valid_index(displayed, index1)
   
    # whether value of two truth list equal or not
        if truth[index1] == truth[index2]:
            displayed[index1] = truth[index1]
            displayed[index2] = truth[index2]
            print("Match!")
        else:
            print(f"Value at index {index1} is {truth[index1]}")
            print(f"Value at index {index2} is {truth[index2]}")
            print("No match. Try again.")
        # to continue
            input("Press Enter to continue...")
        # if don't match
            clear_terminal()
# after winning
    print(displayed)
    print('Congratulations! You won!')
def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
