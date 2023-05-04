"""Question five for an executable examination."""

from typing import List

# TODO: Answer all of the sub-questions inside of this file

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 5a. {{{

# Instructions:
# Implement the requested function so that it operates in the specified fashion

# Function description:
# The function compute_cube should:
# --> Accept as input one int value called input_one
# --> Using any appropriate approach compute and return the cube of that number
# --> For instance, if input_one is equal to 1 then this function would return 1
# --> For instance, if input_one is equal to 2 then this function would return 8


def compute_cube(input_one: int) -> int:
    """Use any approach that can cube an input number."""
    cube_output = 0
    return cube_output


def question_five_a():
    """Run question five-a."""
    # Do not edit this function
    space = " "
    question_five_output_a = str(compute_cube(1))
    question_five_output_a = question_five_output_a + space + str(compute_cube(2))
    question_five_output_a = question_five_output_a + space + str(compute_cube(3))
    return question_five_output_a


# }}}

# Question 5b. {{{

# Instructions:
# Fix the defect(s) in the following function

# Function description:
# The function get_maximum should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is greater than or equal to input_two
#     then the function should return the value of input_one
# --> Otherwise, it should return the value of input_two


def get_maximum(input_one: int, input_two: int) -> int:
    """Return the maximum value of two input values."""
    if input_one <= input_two:
        return input_one
    return input_two


def question_five_b():
    """Run question five-b."""
    # Do not edit this function
    space = " "
    question_five_output_b = str(get_maximum(12, 10))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 9))
    question_five_output_b = question_five_output_b + space + str(get_maximum(3, 3))
    return question_five_output_b

# }}}

# Question 5c. {{{

# Instructions:
# Implement the following function so that it meets the following description

# Function description:
# The function compute_intersection should:
# --> Accept as input two lists of integer values, that may potentially contain duplicate values
# --> Compute the intersection of the two lists and return it as a list of integer values,
# ensuring that the output list does not contain any duplicate values

# For instance, if the function receives the inputs:
# [12, 10] and [9, 10, 11]
# then it would produce as output:
# [10]

# Note that in this example the use of the starting and ending brackets (i.e., [ and ])
# designates that the integer values are contained inside of a list

# Additionally, if the two input lists do not have any values in common
# then the function should return the output value of [], to designate an empty list


def compute_intersection(input_one: List[int], input_two: List[int]) -> List[int]:
    """Compute the intersection of two lists of integers, returning a resulting list without duplicates."""
    intersection_list = []
    return intersection_list


def question_five_c():
    """Run question five-c."""
    # Do not edit this function
    separator = " / "
    question_five_output_c = str(compute_intersection([12, 10], [9, 10, 11]))
    question_five_output_c = question_five_output_c + separator + str(compute_intersection([1, 2, 3], [9, 10, 11]))
    question_five_output_c = question_five_output_c + separator + str(compute_intersection([2, 2, 3], [1, 2, 3]))
    return question_five_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_five():
    """Run all of the subquestions in question five."""
    # call the function for question five-a
    output = question_five_a()
    print(output)
    # call the function for question five-b
    output = question_five_b()
    print(output)
    # call the function for question five-c
    output = question_five_c()
    print(output)


if __name__ == "__main__":
    run_question_five()
