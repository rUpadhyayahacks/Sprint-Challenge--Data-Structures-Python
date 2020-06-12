

from collections import deque
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # We are Doing something not Finding something. No need to return
    def insert(self, value):
        # check if the incoming value is less than the current node's value
        node = BST(value)

        if value < self.value:
            # go left
            if not self.left:
                # if there is no left
                # we can park our node there
                self.left = node
            else:
                # we can't park here
                # keep searching
                self.left.insert(value)
        else: 
            # go right
            if not self.right:
                self.right = node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # with recursion you need a stopping point. In this case it's when we found the target
        #
        #
        # Criteria for returning False: we know we need to go in one direction but there's nothing in that direction
        #
        if target == self.value:
            return True
        if target < self.value:
            # go left
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)
    


    # Return the maximum value found in the tree
    # We are Finding something not Doing something
    # That is why we need to return something out of this method
    def get_max(self):
        max_value = self.value
        if self.right:
            max_value = self.right.get_max()
        return max_value


    # Iterative get_max()
    # self is the root node you are starting from
    def iterative_get_max(self):
        current_max = self.value

        # need to set a pointer
        current = self

        while current is not None:
            if current.value > current_max:
                current_max = current.value
            
            # update our current_max variable if we see a larger value

            current = current.right
        
        return current_max

        # traverse our structure
        # update our current_max variable if we see a larger value

    # Call the function `fn` on the value of each node
    # pass in a function that you want run on every node value
    # we are doing something 
    def for_each(self, fn):
        # call the fn on the value at this node
        fn(self.value)
        # passes the function to the left child
        if self.left:
            self.left.for_each(fn)
        # passes the function to the right child
        if self.right:
            self.right.for_each(fn)
    
    # Iterative for_each
    # Depth-First traversal
    # LIFO ordering of the tree elements (stack ordering)

    def iterative_for_each(self, fn):
        stack = []

        # add the root node
        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)
            
            fn(current.value)


   




    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.right.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        
        # treat passed in node as the root node to the queue
        queue.append(node)

        while len(queue) > 0:
            print(queue[0].value)
            node = queue.popleft()
           
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)

        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []

        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            print(current.value)


    """ breadth first/iterate for queues and depth first/recursion for stacks
    """




    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)
        

    # Print Post-order recursive DFT
    # Post-order traverses the left side first, then the right side of the tree, and ends on the root
    def post_order_dft(self, node):
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)