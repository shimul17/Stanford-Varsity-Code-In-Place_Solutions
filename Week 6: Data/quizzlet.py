def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    # variable for counting correct answer
    correct_count = 0
    # how many words availabe
    total_words = len(translations)
    # loop for every key and value
    for english_word, spanish_translation in translations.items():
        # for user input
        user_answer = input(f'What is the Spanish translation for {english_word}? ')
        # to convert user input to lowercase
        if user_answer.strip().lower() == spanish_translation.lower():
            print("That is correct!")
            correct_count += 1
        else:
             print(f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}.")
        # for printing 1 blank line after every questions
        print()
    # final result    
    print(f"You got {correct_count}/{total_words} words correct, come study again soon!")           
if __name__ == '__main__':
    main()
