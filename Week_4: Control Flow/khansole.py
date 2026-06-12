'''''randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.''''''
import random

def main():
    print("Khansole Academy")
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    expected_answer = num1 + num2
    print(f"What is {num1} + {num2}?")
    user_answer = int(input("Your answer: "))
    
    if user_answer == expected_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {expected_answer}")  
        
if __name__ == '__main__':
    main()
