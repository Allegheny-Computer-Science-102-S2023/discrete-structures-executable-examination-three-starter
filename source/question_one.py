"""Question one for an executable examination."""

from typing import Tuple

# TODO: Answer all of the sub-questions inside of this file

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output


# Question 1a. {{{

# Instructions:
# Implement the following function

# Function description:
# The function determine_even_odd should:
# For the first output value:
# --> Return "even" (of type string) when the input variable (of type int)
#     contains an even number as its value
# --> Return "odd" (of type string) when the input variable (of type int)
#     contains an odd number as its value
# For the second output value:
# --> Return the input number that was provided as an int

# For instance, if the input number to def determine_even_odd was 10
# then the output would be: ("even", 10)
# where the output values are stored in a tuple with
# the first value stored in a string and the second stored in an int


def determine_even_odd(value: int) -> Tuple[str, int]:
    """Determine if a number is even or odd."""
    return ("0", 0)


def question_one_a():
    """Run question one-a."""
    # Do not edit this function
    separator = " / "
    question_one_output_a = str(determine_even_odd(10))
    question_one_output_a = question_one_output_a + separator + str(determine_even_odd(11))
    question_one_output_a = question_one_output_a + separator + str(determine_even_odd(-11))
    question_one_output_a = question_one_output_a + separator + str(determine_even_odd(0))
    return question_one_output_a


# }}}

# Question 1b. {{{

# Instructions:
# Implement the following function

# Function description:
# The function compute_square should:
# --> Accept as input a variable called value of type int
# --> Produce as output an int that is the square of the input value
# --> For instance, an input of 5 would produce the output of 25
# --> The function must use a while loop to perform the computation
# --> Note that it is not acceptable for the compute_square function
#     to use the built-in multiplication operator in Python
# For instance, if the function received the input of 100 it would
# return the output of 100, which is the value of 10 squared.

def compute_square_for(value: int) -> int:
    """Square the square of a number through iteration with a while loop."""
    return 0


def question_one_b():
    """Run question one-b."""
    # Do not edit this function
    space = " "
    question_one_output_b = str(compute_square_for(10))
    question_one_output_b = question_one_output_b + space + str(compute_square_for(-10))
    question_one_output_b = question_one_output_b + space + str(compute_square_for(0))
    return question_one_output_b


# }}}

# Question 1c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function compute_summation should:
# --> Accept as input an int value called maximum
# --> Produce as output an int that is the summation
#     of all the values from 1 to the maximum-1
# --> For instance, if the function receives 5 as
#     input it would perform the computation 1+2+3+4 and
#     return the int value of 10 as output.


def compute_summation(maximum: int) -> int:
    """Compute the summation of the first value numbers."""
    return 0


def question_one_c():
    """Run question one-c."""
    # Do not edit this function
    space = " "
    question_one_output_c = str(compute_summation(5))
    question_one_output_c = question_one_output_c + space + str(compute_summation(6))
    question_one_output_c = question_one_output_c + space + str(compute_summation(7))
    return question_one_output_c


# }}}

# Do not edit any of the source code below this line

def run_question_one():
    """Run all of the subquestions in question one."""
    # call the function for question one-a
    output = question_one_a()
    print(output)
    # call the function for question one-b
    output = question_one_b()
    print(output)
    # call the function for question one-c
    output = question_one_c()
    print(output)


if __name__ == "__main__":
    run_question_one()
