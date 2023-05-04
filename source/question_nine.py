"""Question nine for an executable examination."""

from typing import List
from typing import Tuple

# TODO: Answer all of the sub-questions inside of this file

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Question 9a. {{{

# Instructions:
# Repair any defects inside of this function
# so that it operates in the specified fashion

# Function description:
# The function calculate_powers_of_two_for_loop should:
# --> Accept as input a minimum and a maximum value for computing 2 to the power
#     of a specific number between the inclusive minimum and the exclusive maximum
# --> Store all of the values that result from performing the exponentiation in a list
#     and return them to the calling function
# --> For instance, when the function has the following inputs it will produce the stated outputs
#     Input: 2 for the minimum and 5 for the maximum
#     Output: [4, 8, 16]
# Note that this function must perform the computation using a for loop


def calculate_powers_of_two_for_loop(minimum: int, maximum: int) -> List[int]:
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    powers_list = []
    for i in range(minimum, maximum):
        powers_list.append(i)
    return powers_list


def question_nine_a():
    """Run question nine-a."""
    # Do not edit this function
    separator = " / "
    question_nine_output_a = str(calculate_powers_of_two_for_loop(2, 5))
    question_nine_output_a = question_nine_output_a + separator + str(calculate_powers_of_two_for_loop(0, 5))
    question_nine_output_a = question_nine_output_a + separator + str(calculate_powers_of_two_for_loop(1, 10))
    return question_nine_output_a

# }}}

# Question 9b. {{{

# Instructions:
# Implement this function so that it operates in the specified fashion

# Function description:
# The function calculate_powers_of_two_while_loop should:
# --> Accept as input a minimum and a maximum value for computing 2 to the power
#     of a specific number between the inclusive minimum and the exclusive maximum
# --> Store all of the values that result from performing the exponentiation in a list
#     and return them to the calling function
# --> For instance, when the function has the following inputs it will produce the stated outputs
#     Input: 2 for the minimum and 5 for the maximum
#     Output: [4, 8, 16]
# --> Note that this function must perform the computation using a while loop


def calculate_powers_of_two_while_loop(minimum: int, maximum: int) -> List[int]:
    """Calculate and return the powers of 2 from an inclusive minimum to an exclusive maximum."""
    return [0]


def question_nine_b():
    """Run question nine-b."""
    # Do not edit this function
    separator = " / "
    question_nine_output_b = str(calculate_powers_of_two_while_loop(1, 5))
    question_nine_output_b = question_nine_output_b + separator + str(calculate_powers_of_two_while_loop(1, 10))
    question_nine_output_b = question_nine_output_b + separator + str(calculate_powers_of_two_while_loop(4, 5))
    return question_nine_output_b

# }}}

# Question 9c. {{{

# Instructions:
# Implement the following function so that it produces output
# according to the following function description

# Function description:
# The function determine_relationship should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is less than input_two
#     then the function should return a tuple containing (input_one, input_two, "<")
# --> If the value in input_one is greater than input_two
#     then the function should return a tuple containing (input_one, input_two, ">")
# --> If the value in input_one is exactly equal to input_two
#     then the function should return a tuple containing (input_one, input_two, "=")

# For instance, if the function is provided with the following input it
# will produce the specified output:
# --> Input one = 12, Input two = 10 produces the output (12, 10, '>')
# --> Input one = 10, Input two = 12 produces the output (10, 12, '<')
# --> Input one = 10, Input two = 10 produces the output (10, 10, '=')


def determine_relationship(input_one: int, input_two: int) -> Tuple[int, int, str]:
    """Determine the numerical relationship between the two input values."""
    return (input_one, input_two, "=")


def question_nine_c():
    """Run question nine-c."""
    # Do not edit this function
    separator = " / "
    question_nine_output_c = str(determine_relationship(12, 10))
    question_nine_output_c = question_nine_output_c + separator + str(determine_relationship(3, 9))
    question_nine_output_c = question_nine_output_c + separator + str(determine_relationship(2, 2))
    return question_nine_output_c

# }}}


# Do not edit any of the source code below this line


def run_question_nine():
    """Run all of the subquestions in question nine."""
    # call the function for question nine-a
    output = question_nine_a()
    print(output)
    # call the function for question nine-b
    output = question_nine_b()
    print(output)
    # call the function for question nine-c
    output = question_nine_c()
    print(output)


if __name__ == "__main__":
    run_question_nine()
