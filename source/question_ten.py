"""Question ten for an executable examination."""

from typing import List

# TODO: Answer all of the sub-questions inside of this file

# TOOD: Answer each sub-question and then save and commit and push your work
#       so that you can confirm through GitHub Actions whether your answer is correct or not

# TODO: Please bear in mind that you are responsible for fixing any
#       defects that you introduce into these functions that cause
#       the overall program to crash and/or produce unexpected output

# Class definitions for Question 10 {{{

# Do not modify the source code for these class definitions


class Node:
    """A node structure that stores data and references to left and right children."""

    def __init__(self, value):
        """Construct a new instance of a Node."""
        self.left = None
        self.data = value
        self.right = None

    def __str__(self) -> str:
        """Return a textual representation of a node."""
        return f"{self.data}"


class Tree:
    """A hierarchical tree structure that stores nodes in the form of a binary tree."""

    def __init__(self):
        """Construct a new instance of a Tree."""
        self.traversal = ""
        self.space = " "

    def get_traversal(self) -> str:
        """Return the traversal string."""
        return self.traversal

    def createNode(self, data):
        """Create a new node that will contain the provided data value."""
        return Node(data)

    def insert(self, node, data):
        """Insert a new node with data into the tree."""
        # if tree is empty, return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent, insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def search(self, node, data):
        """Search through the tree to find a node with specific data."""
        # if root is None or root is the search data
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def traverseInorder(self, root):
        """Traverse the tree in an in-order fashion."""
        if root is not None:
            self.traverseInorder(root.left)
            self.traversal = self.traversal + str(root.data) + self.space
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """Traverse the tree in a pre-order fashion."""
        if root is not None:
            self.traversal = self.traversal + str(root.data) + self.space
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """Traverse the tree in a post-order fashion."""
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            self.traversal = self.traversal + str(root.data) + self.space

# }}}

# Question 10a. {{{

# Instructions:
# Construct a tree so that it produces an in-order traversal output
# Please note that to answer this question you should know the
# definition of the term "in-order traversal"
# To produce the output that results from performing the traversal
# this function should call and return the output of tree.get_traversal()

# Important:
# The function must produce the following in-order traversal output:
# 10 50 90 100 120 150 200


def construct_tree() -> str:
    """Construct a tree using the provided classes and methods so that the in-order traversal produces the expected output."""
    root = None
    tree = Tree()
    root = tree.insert(root, 100)
    return tree.get_traversal()


def question_ten_a():
    """Run question ten-a."""
    # Do not edit this function
    question_ten_output_a = str(construct_tree())
    question_ten_output_a = str(construct_tree())
    return question_ten_output_a

# }}}


# Question 10b. {{{

# Instructions:
# Use the same constructed tree from part (a)
# and then call search to produce the following expected output:
# ['100', 'None', '200']

# Note that the output for this question cannot be "hard coded" so
# that it produces the requested output without using the tree.
# It must produce its output through calls to the search function
# as it searches for three different values that produce the
# expected output given previously for part (b).

def search_tree_part_b() -> List[str]:
    """After constructing the same tree from part (a), search for values to produce the expected output."""
    return ['', '', '']


def question_ten_b():
    """Run question ten-b."""
    # Do not edit this function
    question_ten_output_b = str(search_tree_part_b())
    return question_ten_output_b

# }}}

# Question 10c. {{{

# Instructions:
# Use the same constructed tree from part (a)
# and then call search to produce the following expected output:
# ['150', 'None', '120']

# Note that the output for this question cannot be "hard coded" so
# that it produces the requested output without using the tree.
# It must produce its output through calls to the search function
# as it searches for three different values that produce the
# expected output given previously for part (c)


def search_tree_part_c() -> List[str]:
    """After constructing the same tree from part (a), search for values to produce the expected output."""
    return ['', '', '']


def question_ten_c():
    """Run question ten-c."""
    # Do not edit this function
    question_ten_output_c = str(search_tree_part_c())
    return question_ten_output_c

# }}}


# Do not edit any of the source code below this line


def run_question_ten():
    """Run all of the subquestions in question ten."""
    # call the function for question ten-a
    output = question_ten_a()
    print(output)
    # call the function for question ten-b
    output = question_ten_b()
    print(output)
    # call the function for question ten-c
    output = question_ten_c()
    print(output)


if __name__ == "__main__":
    run_question_ten()
