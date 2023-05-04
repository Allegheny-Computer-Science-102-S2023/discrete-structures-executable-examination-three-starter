"""Question six for an executable examination."""

from typing import List
from typing import Tuple

# TODO: Answer all of the sub-questions inside of this file

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 6a. {{{

# Instructions:

# Implement the following function that creates a containing list of singleton
# tuples (i.e., it will make a list of tuples that contain only a single value)

# Function description:
# The function create_singleton_tuples should:
# --> Return a list that contains a total of count singleton tuples
#     that each contain within them the specified value
# --> For instance,
#     -- create_singleton_tuples(1, 10) will create the output [(10,)] because
#     the function was instructed to create 1 singleton tuple that contains the value of 10
#     -- create_singleton_tuples(2, 10) will create the output [(10,), (10,)] because
#     the function was instructed to create 2 singleton tuples that contains the value of 10


def create_singleton_tuples(count: int, value: int) -> List[Tuple[int]]:
    """Create a list containing count singleton tuples each with the specified value."""
    return []


def question_six_a():
    """Run question six-a."""
    # Do not edit this function
    separator = " / "
    question_six_output_a = str(create_singleton_tuples(1, 10))
    question_six_output_a = question_six_output_a + separator + str(create_singleton_tuples(2, 10))
    question_six_output_a = question_six_output_a + separator + str(create_singleton_tuples(3, 10))
    question_six_output_a = question_six_output_a + separator + str(create_singleton_tuples(4, 10))
    question_six_output_a = question_six_output_a + separator + str(create_singleton_tuples(5, 10))
    return question_six_output_a

# }}}

# Question 6b. {{{

# Instructions:

# Implement the following function that creates a containing list of empty
# lists (i.e., a list that contains lists that do not have any contents)

# Function description:
# The function create_empty_lists should:
# --> Return a list that contains a total of count empty lists
# --> For instance,
#     -- create_empty_lists(1) will create the output [[]] because
#     the function was instructed to create a list that contains 1 empty list
#     -- create_empty_lists(2) will create the output [[], []] because
#     the function was instructed to create 2 empty lists in the containing list


def create_empty_lists(count: int) -> List[List[int]]:
    """Create a list containing count empty lists."""
    return []


def question_six_b():
    """Run question six-b."""
    # Do not edit this function
    separator = " / "
    question_six_output_b = str(create_empty_lists(1))
    question_six_output_b = question_six_output_b + separator + str(create_empty_lists(2))
    question_six_output_b = question_six_output_b + separator + str(create_empty_lists(3))
    question_six_output_b = question_six_output_b + separator + str(create_empty_lists(4))
    question_six_output_b = question_six_output_b + separator + str(create_empty_lists(5))
    return question_six_output_b

# }}}

# Question 6c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function compute_summation should:
# --> Accept as input an int value called maximum
# --> Produce as output a tuple that contains:
#     - the value of the maximum parameter
#     - the total count of numbers that were summed together
#     - an int that is the summation of all the values from 1 to the maximum-1
# --> For instance, if the function receives 5 as input
#     it would perform the computation 1+2+3+4 and return:
#     (5, 4, 10) as the output
#     In this example, the number 5 designates the input value of maximum
#     ... and the number 4 designates the total count of numbers summed
#     ... and the number 10 designates the summation of the numbers


def compute_summation(maximum: int) -> Tuple[int, int, int]:
    """Compute the summation of the first value numbers."""
    return (0, 0, 0)


def question_six_c():
    """Run question six-c."""
    # Do not edit this function
    space = " "
    question_six_output_c = str(compute_summation(5))
    question_six_output_c = question_six_output_c + space + str(compute_summation(6))
    question_six_output_c = question_six_output_c + space + str(compute_summation(7))
    return question_six_output_c

# }}}

# Do not edit any of the source code below this line


def run_question_six():
    """Run all of the subquestions in question six."""
    # call the function for question six-a
    output = question_six_a()
    print(output)
    # call the function for question six-b
    output = question_six_b()
    print(output)
    # call the function for question six-c
    output = question_six_c()
    print(output)


if __name__ == "__main__":
    run_question_six()
