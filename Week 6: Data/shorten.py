MAX_LENGTH = 3

def shorten(lst):
    """
    Takes the provided list and removes elements from the end of the list--
    printing each removed element out--until the list has at most MAX_LENGTH
    elements inside of it.
    """
    
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(removed_element)

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()
