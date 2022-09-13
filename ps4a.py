# Problem Set 4a
# Name: Autumn Artist
# Collaborators: Daniel Ajayi
# Time Spent: 12:00

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(5)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(4), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(19), Node(26))))



def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    #Counting the right and left children
    left = 0
    right = 0
    #Case: no right or left children
    if Node.get_left_child(tree) == None and Node.get_right_child(tree) == None:
        return 0
    else:
        #Case has left child
        if Node.get_left_child(tree) != None:
            left += 1
            left += find_tree_height(Node.get_left_child(tree))
        #Case: has right child
        if Node.get_right_child(tree) != None:
            right += 1 
            right += find_tree_height(Node.get_right_child(tree))    
    return max(left, right)

def is_heap(tree,compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    #No left child - automatically the max or min
    if Node.get_left_child(tree) == None:
        heap_left = True
    else:
        #If compare = true, run the method again
        if compare_func(Node.get_value(Node.get_left_child(tree)), Node.get_value(tree)) == True:
            heap_left = is_heap(Node.get_left_child(tree), compare_func)
        else:
            #compare = False - everything false, return false
            return False
    #No right child - automatically max or min 
    if Node.get_right_child(tree) == None:
        heap_right = True
    else:
        #compare = true, run method again
        if compare_func(Node.get_value(Node.get_right_child(tree)), Node.get_value(tree)) == True:
            heap_right = is_heap(Node.get_right_child(tree), compare_func)
        else:
            #compare = false, everything false
            return False
        #only return true if both left and right are true
    if (heap_left and heap_right) == True:
        return True
        

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code\
    
    pass