#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: March 28, 2022
# This program asks the user for a number
# then if check if the number is positive,
# negative or 0 and display them the answer.


# set random number


def main():
    # ask user for a number between 1-9
    the_number = int(input("Enter a number "))
    print("")

    # check if what type of number they entered
    # and dispay the answer
    if the_number > 0:
        print(the_number, "is a positive number")
    elif the_number < 0:
        print(the_number, "is a negative number")
    elif the_number == 0:
        print(the_number, "is just a 0")


if __name__ == "__main__":
    main()
