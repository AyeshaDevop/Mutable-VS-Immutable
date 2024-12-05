def add_three_copies(my_list, data):
    """
    Appends three copies of 'data' to 'my_list'. This demonstrates mutability,
    as changes to the list are reflected outside this function.
    """
    for i in range(3):
        my_list.append(data)
def main():
    """
    Demonstrates the mutability of lists by adding three copies of user-provided
    data to a list and displaying the changes.
    """
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()