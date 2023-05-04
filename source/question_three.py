"""Question three for an executable examination."""

from pathlib import Path
from typing import List

# TODO: Answer all of the sub-questions inside of this file

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output


# Question 3a. {{{

# Instructions:
# Implement the source code lines in this function
# so that it operates in the specified fashion

# Function description:
# The function input_file should:
# --> Accept as input a file_name that is of type string
# --> Assume that the program that runs the function will
#     be executed from the root of the GitHub repository;
#     as in "python source/question_three.py"
# --> Construct a pathlib Path object and then read in the
#     values from the file and store them as strings in a list
# --> Return a list of strings containing all of the values
#     that were stored inside of the file.
# --> For instance, the inputs/observations.txt file contains these values:
#     5
#     7
#     9
#     11
#
#     This means that it would cause this function to produce the output:
#     ['5', '7', '9', '11']


def input_file(file_name: str) -> List[str]:
    """Use a pathlib Path object to read and return the contents of the specified file."""
    return [""]


def question_three_a():
    """Run question three-a."""
    # Do not edit this function
    question_three_output_a = input_file("inputs/observations.txt")
    return question_three_output_a

# }}}

# Question 3b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function convert_list should:
# --> Accept as input a variable called input_list that contains a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a list of all the converted int values
# --> For instance, when the function receives the input ['5', '7', '9', '11']
#     if will produce the output [5, 7, 9, 11]


def convert_list(input_list: List[str]) -> List[int]:
    """Convert a list of strings to a list of int values."""
    output_list_int = []
    for input_value in input_list:
        input_value_int = int(input_value)
    return output_list_int


def question_three_b():
    """Run question three-b."""
    # Do not edit this function
    question_tree_output_b = convert_list(['5', '7', '9', '11'])
    return question_tree_output_b

# }}}

# Question 3c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function compute_fibonacci should:
# --> Recursively compute the number in the Fibonacci sequence for the specific input number
# For instance, when provided with the input of 7 it will recursively compute the sequence:
# 1 1 2 3 5 8 13
# and then since 13 is the seventh number in the sequence it will return it as the output
# --> It must also use an LRU cache with a maximum size of 128 so that it can
# automatically leverage a dictionary to ensure that previously computed values are not re-computed

import functools  # noqa


def compute_fibonacci(input_number: int) -> int:
    """Compute the requested number in the Fibonacci sequence using an LRU cache to improve performance."""
    return 0


def question_three_c():
    """Run question three-c."""
    # Do not edit this function
    separator = " / "
    question_one_output_a = str(compute_fibonacci(7))
    question_one_output_a = question_one_output_a + separator + str(compute_fibonacci(6))
    question_one_output_a = question_one_output_a + separator + str(compute_fibonacci(5))
    return question_one_output_a

# }}}

# Do not edit any of the source code below this line


def run_question_three():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_three_a()
    print(output)
    # call the function for question three-b
    output = question_three_b()
    print(output)
    # call the function for question three-c
    output = question_three_c()
    print(output)


if __name__ == "__main__":
    run_question_three()
