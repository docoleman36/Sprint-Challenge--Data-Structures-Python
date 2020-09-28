"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if self.value is target
        if self.value is target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            elif self.left.value == target:
                return True
            else:
                self.left.contains(target)
        else:
            if not self.right:
                return False
            elif self.right.value == target:
                return True
            else:
                self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # go right until you cannot anymore
        # return value at far right
        if self.right is None:
            return self.value
        else:
            cur_node = self.right
            while cur_node.right is not None:
                cur_node = cur_node.right
            return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is None and self.right is None:
            return

        # go left, call fn(value) for each node
        if self.left:
            self.left.for_each(fn)
        # go roght, call fn(value) for each node
        if self.right:
            self.right.for_each(fn)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
