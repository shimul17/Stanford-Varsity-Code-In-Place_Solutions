def main():
    values = []
    # start a unlimited loop
    while True:
        user_input = input("Enter a value: ")
        # if user don't write anything and press enter
        if user_input == "":
            break
        # for connecting input to the last of list
        values.append(user_input)
    # after finshing loop to do print whole list
    print("Here's the list:", values)

if __name__ == '__main__':
    main()
