# Node initial
class Node:
    # Each node will have two things associated with it: the probability of it happening, and the name of the event
    def __init__(self, probability, name_event):
        self.probability = probability
        self.name_event = name_event
        self.left_child = None
        self.level = None
        self.right_child = None

    def add_left_child(self, child_node):
        self.left_child = child_node

    def add_right_child(self, child_node):
        self.right_child = child_node
    def add_level(self,level):
        self.level = level
    def return_prob(self):
        return self.probability
    def return_name(self):
        return self.name_event



name = input("Enter name for tree diagram: ")
main = [Node(1, name)]
def search(parent_name, child_name, p):
    for node in main
# what it extends out of ie: X<XX<XXXX<XXXXXXXX
# this is based on a AP Stat type of tree diagram, so each level has 2^n items, where n < L, and L is the depth of the tree
#include initial level when entering
j = int(input("Enter the number of levels to your tree diagram(depth): "))

for i in range(j-1):
    for k in range(2**(j-1)):
        name_parent = input("Enter name of the parent event: ")
        name_child = input("Enter name of the child event: ")
        prob = float(input("Enter probability of event happening(ex: .75): "))
        search(name_parent, name_child, prob)
            

    
