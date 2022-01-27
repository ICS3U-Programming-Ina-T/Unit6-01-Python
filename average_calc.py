#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 27, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the average to the console

import constants
import random


def main():
    # initializing  sum and counter
    sum = 0
    counter = 0
    
    # declaring variable
    list_of_ints = []

    # display opening message to console
    print("This program generates a list of random "
          "numbers between 0 and 100, then calculates the average.")
    print("")

    # displays random numbers and calculates average
    for counter in range(constants.MAX_ARRAY_SIZE):
        list_of_ints.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        sum = sum + list_of_ints[counter]
        print("{} added to the list at "
              "position {}" .format(list_of_ints[counter], counter))

    # determine if array is full
    # calculate and display average    
    for counter in range(1):
        average = sum / constants.MAX_ARRAY_SIZE
        print("")
        print("The average is {}" .format(str(average)))


if __name__ == "__main__":
    main()
