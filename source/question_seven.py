"""Question seven for an executable examination."""

from typing import Dict
from typing import List
from typing import Tuple

# TODO: Answer all of the sub-questions inside of this file

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 7a. {{{

# Instructions:
# Implement the following function so that it fulfills its description

# Function description:
# The function compute_difference should:
# --> Accept as input two lists of integer values, that may potentially contain duplicate values
# --> Compute the difference of the two lists and return it as a list of integer values,
# ensuring that the output list does not contain any duplicate values

# For instance, if the function receives the inputs:
# [12, 10] and [9, 10, 11]
# then it would produce as output:
# [12]

# Note that in this example the use of the starting and ending brackets (i.e., [ and ])
# designates that the integer values are contained inside of a list

# Additionally, if the the difference computation results in no values,
# then the function should return the output value of [], to designate an empty list


def compute_difference(input_one: List[int], input_two: List[int]) -> List[int]:
    """Compute the difference of two lists of integers, returning a resulting list without duplicates."""
    return []


def question_seven_a():
    """Run question seven-a."""
    # Do not edit this function
    separator = " / "
    question_seven_a = str(compute_difference([12, 10], [9, 10, 11]))
    question_seven_a = question_seven_a + separator + str(compute_difference([1, 2, 3], [9, 10, 11]))
    question_seven_a = question_seven_a + separator + str(compute_difference([2, 2, 3], [1, 2, 3]))
    return question_seven_a

# }}}

# Question 7b. {{{

# Instructions:
# Implement a function that performs the following operation

# Function description:
# The function convert_list_to_paired_dictionary should:
# --> Accept as input a variable called input_list that is a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a dictionary (i.e., a dict) that maps the string value to the int value
# --> For instance, when the function receives the input ['5', '7', '9', '11']
#     if will produce the output {'5': 5, '7': 7, '9': 9, '11': 11}


def convert_list_to_paired_dictionary(input_list: List[str]) -> Dict[str, int]:
    """Convert a list of strings to a dictionary that maps the strings to their int values."""
    return {"0": 0}


def question_seven_b():
    """Run question three-b."""
    # Do not edit this function
    separator = " / "
    question_seven_output_b = str(convert_list_to_paired_dictionary(['5', '7', '9', '11']))
    question_seven_output_b = question_seven_output_b + separator + str(convert_list_to_paired_dictionary(['1', '2', '3', '4']))
    return question_seven_output_b

# }}}

# Question 7c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function sum_list should:
# --> Accept as input a tuple of four int values
# --> Compute the sum of all of the int values in the tuple
# --> Return the sum of all the int values in the tuple
# --> For instance, if the function receives (5, 7, 9, 11) as
#     an input it returns the dictionary that contains {(5, 7, 9, 11): 32}
# Note that this function is not required to handle any other inputs than
# a tuple that contains four int values


def sum_list(input_list: Tuple[int, int, int, int]) -> Dict[Tuple[int, ...], int]:
    """Sum all of the values inside of a list of int values."""
    return None


def question_seven_c():
    """Run question seven-c."""
    # Do not edit this function
    separator = " / "
    question_seven_output_c = str(sum_list((int(5), int(7), int(9), int(11))))
    question_seven_output_c = question_seven_output_c + separator + str(sum_list((int(1), int(2), int(3), int(4))))
    return question_seven_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_seven():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_seven_a()
    print(output)
    # call the function for question three-b
    output = question_seven_b()
    print(output)
    # call the function for question three-c
    output = question_seven_c()
    print(output)


if __name__ == "__main__":
    run_question_seven()
