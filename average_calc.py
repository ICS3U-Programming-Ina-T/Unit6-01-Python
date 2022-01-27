#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 27, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the average to the console

import constants
import random


def main():
    # initalizing sum and counter
    sum = 0
    counter = 0

    # display opening message to console
    print("This program generates a list of random "
          "numbers between 0 and 100, then calculates the average.")
    print("")

    # displays random numbers and calculates average
    for counter in range(constants.MAX_ARRAY_SIZE):
        list_of_ints = [random.randint(constants.MIN_NUM, constants.MAX_NUM)]
        sum = sum + list_of_ints[0]
        print("{} added to the list at "
              "position {}" .format(list_of_ints[0], counter))

        # determine if array is full
        # calculate and display average
        if counter == 9:
            average = sum / constants.MAX_ARRAY_SIZE
            print("")
            print("The average is {}" .format(str(average)))


if __name__ == "__main__":
    main()
